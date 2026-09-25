from repomind.rag.repository_loader import get_repository_chunks
from repomind.rag.embeddings import create_embeddings
from repomind.rag.vector_store import add_chunk, delete_repository_chunks


def index_repository(
    owner: str,
    repo: str
):
    delete_repository_chunks(owner, repo)

    chunks = get_repository_chunks(owner, repo)

    print("Total chunks:", len(chunks))

    texts = []

    for chunk in chunks:
        texts.append(chunk["content"])

    embeddings = create_embeddings(texts)

    for index, chunk in enumerate(chunks):
        add_chunk(
            chunk_id=f"{owner}-{repo}-{index}",
            content=chunk["content"],
            embedding=embeddings[index],
            file_path=chunk["file"],
            owner=owner,
            repo=repo
        )

        print(f"Indexed chunk {index + 1}/{len(chunks)}")

    return len(chunks)
