import base64

import httpx


def get_repository(
    owner: str,
    repo: str
):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = httpx.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def get_repository_files(
    owner: str,
    repo: str
):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    response = httpx.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def get_repository_folder(
    owner: str,
    repo: str,
    path: str
):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    response = httpx.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def get_repository_file(
    owner: str,
    repo: str,
    path: str
):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    response = httpx.get(url)

    if response.status_code != 200:
        return None

    file_data = response.json()

    content = file_data.get("content")

    if content:
        decoded_content = base64.b64decode(
            content
        ).decode("utf-8")

        file_data["content"] = decoded_content

    return file_data


def get_repository_commits(
    owner: str,
    repo: str
):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = httpx.get(url)

    if response.status_code != 200:
        return None

    commits = response.json()

    result = []

    for commit in commits:
        result.append({
            "sha": commit["sha"],
            "message": commit["commit"]["message"],
            "author": commit["commit"]["author"]["name"],
            "date": commit["commit"]["author"]["date"],
            "url": commit["html_url"]
        })

    return result