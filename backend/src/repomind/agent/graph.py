from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from openai import OpenAI

from repomind.core.config import OPENAI_API_KEY
from repomind.mcp.mcp_client import run_mcp_tool


client = OpenAI(api_key=OPENAI_API_KEY)


class RepoState(TypedDict):
    question: str
    context: str
    answer: str
    tool: str


def decide_tool(state: RepoState):

    print("Deciding which tool to use...")

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

Question:

{state["question"]}

Return only one of these exact values:

search_repository

or

get_commits
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

    context = run_mcp_tool(
        "search_repository",
        {
            "question": state["question"]
        }
    )

    return {
        "context": context
    }


def get_commits_node(state: RepoState):

    print("Getting commits...")

    context = run_mcp_tool(
        "get_commits",
        {}
    )

    return {
        "context": context
    }


def generate_answer(state: RepoState):

    print("Generating answer...")

    prompt = f"""
You are RepoMind, an AI assistant that answers
questions about a GitHub repository.

Use the repository context below to answer the question.

If the answer is not available in the context,
say that you could not find the answer in the repository.

Repository context:

{state["context"]}

Question:

{state["question"]}
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

    answer = response.choices[0].message.content

    return {
        "answer": answer
    }


def route_tool(state: RepoState):

    if state["tool"] == "get_commits":
        return "get_commits"

    return "search_repository"


graph = StateGraph(RepoState)

graph.add_node("decide_tool", decide_tool)
graph.add_node("search_repository", search_repository_node)
graph.add_node("get_commits", get_commits_node)
graph.add_node("generate_answer", generate_answer)

graph.add_edge(START, "decide_tool")

graph.add_conditional_edges(
    "decide_tool",
    route_tool,
    {
        "search_repository": "search_repository",
        "get_commits": "get_commits"
    }
)

graph.add_edge("search_repository", "generate_answer")
graph.add_edge("get_commits", "generate_answer")
graph.add_edge("generate_answer", END)

app = graph.compile()
