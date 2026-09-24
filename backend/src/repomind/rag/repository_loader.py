from src.repomind.services.github_service import (
    get_repository_files,
    get_repository_file
)

from src.repomind.rag.splitter import split_text


def get_repository_chunks(
    owner: str,
    repo: str
):

    files = get_repository_files(
        owner,
        repo
    )

    if files is None:
        return []


    all_chunks = []


    for file in files:

        if file["type"] != "file":
            continue


        file_data = get_repository_file(
            owner,
            repo,
            file["path"]
        )

        if file_data is None:
            continue


        content = file_data.get("content")

        if not content:
            continue


        chunks = split_text(content)


        for chunk in chunks:

            all_chunks.append({
                "file": file["path"],
                "content": chunk
            })


    return all_chunks