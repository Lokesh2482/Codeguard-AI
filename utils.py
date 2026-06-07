# General utilities for the project
def clean_repo_url(url: str) -> str:
    return url.strip().rstrip("/")
