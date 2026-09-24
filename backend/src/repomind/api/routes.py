from fastapi import APIRouter
from sqlalchemy import text

from repomind.db.database import engine

from repomind.services.github_service import (
    get_repository,
    get_repository_files,
    get_repository_folder,
    get_repository_file,
    get_repository_commits
)


router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to RepoMind"
    }


@router.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e),
        }


@router.get("/github/{owner}/{repo}")
def github_repository(
    owner: str,
    repo: str
):
    repository = get_repository(
        owner,
        repo
    )

    if repository is None:
        return {
            "message": "Repository not found"
        }

    return {
        "name": repository["name"],
        "full_name": repository["full_name"],
        "description": repository["description"],
        "language": repository["language"],
        "stars": repository["stargazers_count"],
        "forks": repository["forks_count"],
        "url": repository["html_url"],
    }


@router.get("/github/{owner}/{repo}/files")
def github_repository_files(
    owner: str,
    repo: str
):
    files = get_repository_files(
        owner,
        repo
    )

    if files is None:
        return {
            "message": "Repository files not found"
        }

    return files


@router.get("/github/{owner}/{repo}/files/{path:path}")
def github_repository_folder(
    owner: str,
    repo: str,
    path: str
):
    files = get_repository_folder(
        owner,
        repo,
        path
    )

    if files is None:
        return {
            "message": "Folder not found"
        }

    return files


@router.get("/github/{owner}/{repo}/file/{path:path}")
def github_repository_file(
    owner: str,
    repo: str,
    path: str
):
    file = get_repository_file(
        owner,
        repo,
        path
    )

    if file is None:
        return {
            "message": "File not found"
        }

    return file


@router.get("/github/{owner}/{repo}/commits")
def github_repository_commits(
    owner: str,
    repo: str
):
    commits = get_repository_commits(
        owner,
        repo
    )

    if commits is None:
        return {
            "message": "Repository commits not found"
        }

    return commits