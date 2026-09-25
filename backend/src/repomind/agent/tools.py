from langchain_core.tools import tool

from repomind.rag.embeddings import create_embedding
from repomind.rag.vector_store import search_chunks
from repomind.services.github_service import get_repository_commits


@tool
def search_repository(question: str) -> str:
    """Search the RepoMind repository for relevant code."""

    question_embedding = create_embedding(question)

    results = search_chunks(
        query_embedding=question_embedding,
        owner="amiteshpandey18",
        repo="RepoMind",
        number_of_results=3
    )

    documents = results["documents"][0]

    if not documents:
        return "No relevant information found in the repository."

    return "\n\n".join(documents)


@tool
def get_commits() -> str:
    """Get recent commits from the RepoMind repository."""

    commits = get_repository_commits(
        "amiteshpandey18",
        "RepoMind"
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