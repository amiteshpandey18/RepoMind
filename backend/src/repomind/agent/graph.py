from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.config import get_stream_writer
from openai import OpenAI
from psycopg import Connection
from psycopg.rows import dict_row

from repomind.core.config import OPENAI_API_KEY, DATABASE_URL
from repomind.mcp.mcp_client import run_mcp_tool


client = OpenAI(api_key=OPENAI_API_KEY)


class RepoState(MessagesState):
    question: str
    context: str
    answer: str
    tool: str
    source: str
    owner: str
    repo: str


def decide_tool(state: RepoState):

    print("Deciding which tool to use...")

    conversation = []

    for message in state["messages"]:
        conversation.append(message.content)

    conversation = "\n".join(conversation)

    prompt = f"""
You are deciding which tool RepoMind should use.

Available tools:

1. search_repository
   Use this for questions about repository code,
   files, configuration, authentication, database,
   APIs, implementation, or how the project works.

2. get_commits
   Use this for questions about commits,
   commit history, recent changes, or repository history.

3. get_issues
   Use this for questions about GitHub issues,
   bugs, problems, or reported tasks.

4. get_pull_requests
   Use this for questions about pull requests,
   PRs, code changes, or proposed changes.

Previous conversation:

{conversation}

Current question:

{state["question"]}

Return only one of these exact values:

search_repository

get_commits

get_issues

get_pull_requests
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    tool = response.choices[0].message.content.strip()

    print("Selected tool:", tool)

    return {
        "tool": tool
    }


def search_repository_node(state: RepoState):

    print("Searching repository...")

    conversation = []

    for message in state["messages"]:
        conversation.append(message.content)

    search_question = "\n".join(conversation)

    context = run_mcp_tool(
        "search_repository",
        {
            "owner": state["owner"],
            "repo": state["repo"],
            "question": search_question
        }
    )

    sources = []

    for line in context.splitlines():

        if line.startswith("File: "):

            file_name = line.replace("File: ", "")

            if file_name not in sources:
                sources.append(file_name)

    source = "\n".join(sources)

    return {
        "context": context,
        "source": source
    }


def get_commits_node(state: RepoState):

    print("Getting commits...")

    context = run_mcp_tool(
        "get_commits",
        {
            "owner": state["owner"],
            "repo": state["repo"]
        }
    )

    return {
        "context": context,
        "source": "GitHub Commits"
    }


def get_issues_node(state: RepoState):

    print("Getting issues...")

    context = run_mcp_tool(
        "get_issues",
        {
            "owner": state["owner"],
            "repo": state["repo"]
        }
    )

    return {
        "context": context,
        "source": "GitHub Issues"
    }


def get_pull_requests_node(state: RepoState):

    print("Getting pull requests...")

    context = run_mcp_tool(
        "get_pull_requests",
        {
            "owner": state["owner"],
            "repo": state["repo"]
        }
    )

    return {
        "context": context,
        "source": "GitHub Pull Requests"
    }


def generate_answer(state: RepoState):

    print("Generating answer...")

    writer = get_stream_writer()

    messages = []

    for message in state["messages"]:
        messages.append(
            f"{message.type}: {message.content}"
        )

    conversation = "\n".join(messages)

    prompt = f"""
You are RepoMind, an AI assistant that answers
questions about a GitHub repository.

Repository:

{state["owner"]}/{state["repo"]}

Use the repository context below to answer the question.

Previous conversation:

{conversation}

Repository context:

{state["context"]}

Current question:

{state["question"]}

If the answer is not available in the repository
or conversation, say that you could not find the
answer in the repository.

Sources:

{state["source"]}

When answering, include exactly one "Sources"
section at the end of your answer.

Under Sources, list the actual files used from the
repository context.

Do not create another source section.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True
    )

    answer = ""

    for chunk in response:

        content = chunk.choices[0].delta.content

        if content:

            answer += content
            writer(content)

    return {
        "answer": answer,
        "messages": [
            {
                "role": "assistant",
                "content": answer
            }
        ]
    }


def route_tool(state: RepoState):

    if state["tool"] == "get_commits":
        return "get_commits"

    if state["tool"] == "get_issues":
        return "get_issues"

    if state["tool"] == "get_pull_requests":
        return "get_pull_requests"

    return "search_repository"


graph = StateGraph(RepoState)

graph.add_node("decide_tool", decide_tool)
graph.add_node("search_repository", search_repository_node)
graph.add_node("get_commits", get_commits_node)
graph.add_node("get_issues", get_issues_node)
graph.add_node("get_pull_requests", get_pull_requests_node)
graph.add_node("generate_answer", generate_answer)

graph.add_edge(START, "decide_tool")

graph.add_conditional_edges(
    "decide_tool",
    route_tool,
    {
        "search_repository": "search_repository",
        "get_commits": "get_commits",
        "get_issues": "get_issues",
        "get_pull_requests": "get_pull_requests"
    }
)

graph.add_edge("search_repository", "generate_answer")
graph.add_edge("get_commits", "generate_answer")
graph.add_edge("get_issues", "generate_answer")
graph.add_edge("get_pull_requests", "generate_answer")

graph.add_edge("generate_answer", END)


# PostgreSQL checkpointer

postgres_url = DATABASE_URL.replace(
    "postgresql+psycopg2://",
    "postgresql://"
)

conn = Connection.connect(
    postgres_url,
    autocommit=True,
    row_factory=dict_row
)

checkpointer = PostgresSaver(conn)

checkpointer.setup()

app = graph.compile(
    checkpointer=checkpointer
)
