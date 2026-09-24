from src.repomind.rag.indexer import index_repository


total_chunks = index_repository(
    "fastapi",
    "fastapi"
)


print()
print("==============================")
print("Repository indexing complete")
print("Total chunks indexed:", total_chunks)
print("==============================")