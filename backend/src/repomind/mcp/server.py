from mcp.server.mcpserver import MCPServer

from repomind.rag.embeddings import create_embedding
from repomind.rag.vector_store import search_chunks
from repomind.services.github_service import (
    get_repository_commits,
    get_repository_issues,
    get_repository_pull_requests
)


mcp = MCPServer("RepoMind")


@mcp.tool()
def search_repository(
    owner: str,
    repo: str,
    question: str
) -> str:
    """Search a GitHub repository for relevant code."""

    question_embedding = create_embedding(question)

    results = search_chunks(
        query_embedding=question_embedding,
        owner=owner,
        repo=repo,
        number_of_results=10
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    if not documents:
        return "No relevant information found in the repository."

    result = []

    for document, metadata in zip(documents, metadatas):
        result.append(
            f"File: {metadata['file']}\n"
            f"Code:\n{document}"
        )

    return "\n\n".join(result)


@mcp.tool()
def get_commits(
    owner: str,
    repo: str
) -> str:
    """Get recent commits from a GitHub repository."""

    commits = get_repository_commits(
        owner,
        repo
    )

    if not commits:
        return "No commits found."

    result = []

    for commit in commits:
        result.append(
            f"Commit: {commit['sha']}\n"
            f"Message: {commit['message']}\n"
            f"Author: {commit['author']}\n"
            f"Date: {commit['date']}\n"
            f"URL: {commit['url']}"
        )

    return "\n\n".join(result)


@mcp.tool()
def get_issues(
    owner: str,
    repo: str
) -> str:
    """Get issues from a GitHub repository."""

    issues = get_repository_issues(
        owner,
        repo
    )

    if not issues:
        return "No issues found."

    result = []

    for issue in issues:
        result.append(
            f"Issue: #{issue['number']}\n"
            f"Title: {issue['title']}\n"
            f"State: {issue['state']}\n"
            f"Author: {issue['author']}\n"
            f"URL: {issue['url']}"
        )

    return "\n\n".join(result)


@mcp.tool()
def get_pull_requests(
    owner: str,
    repo: str
) -> str:
    """Get pull requests from a GitHub repository."""

    pull_requests = get_repository_pull_requests(
        owner,
        repo
    )

    if not pull_requests:
        return "No pull requests found."

    result = []

    for pull_request in pull_requests:
        result.append(
            f"PR: #{pull_request['number']}\n"
            f"Title: {pull_request['title']}\n"
            f"State: {pull_request['state']}\n"
            f"Author: {pull_request['author']}\n"
            f"URL: {pull_request['url']}"
        )

    return "\n\n".join(result)


if __name__ == "__main__":
    mcp.run()
