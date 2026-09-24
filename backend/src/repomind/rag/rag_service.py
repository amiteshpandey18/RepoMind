from openai import OpenAI

from repomind.core.config import OPENAI_API_KEY
from repomind.rag.embeddings import create_embedding
from repomind.rag.vector_store import search_chunks


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def ask_repository(
    owner: str,
    repo: str,
    question: str
):

    question_embedding = create_embedding(
        question
    )

    results = search_chunks(
        query_embedding=question_embedding,
        owner=owner,
        repo=repo,
        number_of_results=3
    )

    documents = results["documents"][0]

    if not documents:
        return "I could not find the answer in the repository."

    context = "\n\n".join(documents)

    prompt = f"""
You are RepoMind, an AI assistant that answers
questions about a GitHub repository.

Repository: {owner}/{repo}

Use the repository context below to answer the question.

If the answer is not available in the context,
say that you could not find the answer in the repository.

Repository context:

{context}

Question:

{question}
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

    return response.choices[0].message.content
