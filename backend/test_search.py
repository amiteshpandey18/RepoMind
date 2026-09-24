from src.repomind.rag.embeddings import create_embedding
from src.repomind.rag.vector_store import search_chunks


question = "What is the purpose of this repository?"

question_embedding = create_embedding(
    question
)

results = search_chunks(
    query_embedding=question_embedding,
    owner="amiteshpandey18",
    repo="RepoMind",
    number_of_results=3
)


print("Search Results")
print("================")


for i, document in enumerate(results["documents"][0]):

    metadata = results["metadatas"][0][i]

    print(
        f"\nFile: {metadata['file']}"
    )

    print(
        f"Owner: {metadata['owner']}"
    )

    print(
        f"Repo: {metadata['repo']}"
    )

    print(
        f"Content: {document}"
    )
