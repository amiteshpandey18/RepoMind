import httpx


def get_repository(owner: str, repo: str):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = httpx.get(url)

    if response.status_code != 200:
        return None

    return response.json()