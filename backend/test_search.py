from src.repomind.rag.embeddings import create_embedding
from src.repomind.rag.vector_store import search_chunks


question = "How does FastAPI validate data?"


query_embedding = create_embedding(
    question
)


results = search_chunks(
    query_embedding
)


print("Search Results")
print("================")


for document, metadata in zip(
    results["documents"][0],
    results["metadatas"][0]
):

    print()
    print("File:", metadata["file"])
    print("Content:", document)
