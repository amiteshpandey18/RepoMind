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
    file_path: str,
    owner: str,
    repo: str
):
    collection.add(
        ids=[chunk_id],
        documents=[content],
        embeddings=[embedding],
        metadatas=[
            {
                "file": file_path,
                "owner": owner,
                "repo": repo
            }
        ]
    )


def search_chunks(
    query_embedding: list[float],
    owner: str,
    repo: str,
    number_of_results: int = 3
):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=number_of_results,
        where={
            "$and": [
                {"owner": owner},
                {"repo": repo}
            ]
        }
    )

    return results
