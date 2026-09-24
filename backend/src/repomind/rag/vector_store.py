import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_or_create_collection(
    name="repository_chunks"
)


def add_chunk(
    chunk_id: str,
    content: str,
    embedding: list[float],
    file_path: str
):
    collection.add(
        ids=[chunk_id],
        documents=[content],
        embeddings=[embedding],
        metadatas=[
            {
                "file": file_path
            }
        ]
    )


def search_chunks(
    query_embedding: list[float],
    number_of_results: int = 3
):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=number_of_results
    )

    return results
