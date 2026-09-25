import base64

import httpx

from repomind.core.config import GITHUB_TOKEN


headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def get_repository(
    owner: str,
    repo: str
):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = httpx.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        return None

    return response.json()


def get_repository_files(
    owner: str,
    repo: str,
    path: str = ""
):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    response = httpx.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        return None

    items = response.json()

    all_files = []

    for item in items:

        if item["type"] == "file":

            all_files.append(item)

        elif item["type"] == "dir":

            folder_files = get_repository_files(
                owner,
                repo,
                item["path"]
            )

            if folder_files:
                all_files.extend(folder_files)

    return all_files


def get_repository_folder(
    owner: str,
    repo: str,
    path: str
):
    url = f"https://api.github.com/repos/{owner}/repo/contents/{path}"

    response = httpx.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        return None

    return response.json()


def get_repository_file(
    owner: str,
    repo: str,
    path: str
):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    response = httpx.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        return None

    file_data = response.json()

    content = file_data.get("content")

    if content:

        try:
            decoded_content = base64.b64decode(
                content
            ).decode("utf-8")

            file_data["content"] = decoded_content

        except UnicodeDecodeError:

            file_data["content"] = None

    return file_data


def get_repository_commits(
    owner: str,
    repo: str
):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = httpx.get(
        url,
        headers=headers
    )

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


def get_repository_issues(
    owner: str,
    repo: str
):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"

    response = httpx.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        return None

    issues = response.json()

    result = []

    for issue in issues:

        if "pull_request" in issue:
            continue

        result.append({
            "number": issue["number"],
            "title": issue["title"],
            "state": issue["state"],
            "author": issue["user"]["login"],
            "url": issue["html_url"]
        })

    return result


def get_repository_pull_requests(
    owner: str,
    repo: str
):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

    response = httpx.get(
        url,
        headers=headers
    )

    if response.status_code != 200:
        return None

    pull_requests = response.json()

    result = []

    for pull_request in pull_requests:

        result.append({
            "number": pull_request["number"],
            "title": pull_request["title"],
            "state": pull_request["state"],
            "author": pull_request["user"]["login"],
            "url": pull_request["html_url"]
        })

    return result
