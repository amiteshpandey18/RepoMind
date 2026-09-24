from src.repomind.rag.repository_loader import (
    get_repository_chunks
)


chunks = get_repository_chunks(
    "fastapi",
    "fastapi"
)


print("Total chunks:", len(chunks))


for index, chunk in enumerate(chunks[:5]):

    print()
    print("Chunk", index + 1)
    print("----------------")

    print("File:", chunk["file"])

    print("Content:")
    print(chunk["content"])