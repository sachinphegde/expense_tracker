"""
Methods to interact with github files
"""
import os
import sys
import json
import requests
import base64
from config import GITHUB_TOKEN, DB_LOCAL_PATH, DATABASE_URL, BUDGET_URL, BUDGET_LOCAL_PATH


def get_file_name(file_type):
    """
    Args:
        file_type (String): send the file type to download
        valid options: db and json from now

    Returns:
        String: file URL
        String: file local path to store
    """
    if file_type == "db":
        url = DATABASE_URL
        path = DB_LOCAL_PATH
    elif file_type == "json":
        url = BUDGET_URL
        path = BUDGET_LOCAL_PATH
    else:
        print("Error: No file mentioned for download via github")
        sys.exit(1)
    return url, path


def download_from_github(file_type):
    """
    Downloads the required file from GitHub into the specified path.
    """
    url, path = get_file_name(file_type)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()

    download_url = r.json()["download_url"]
    db_content = requests.get(download_url, timeout=10)
    with open(path, "wb") as f:
        f.write(db_content.content)

    filename = url.rsplit('/', 1)[-1]
    print(f"Downloaded {filename} to {path}")


def upload_to_github(file_type):
    """
    Uploads the local modified file to GitHub.
    """
    url, path = get_file_name(file_type)
    # Get SHA of existing file
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()

    sha = resp.json()["sha"]

    # Read and base64 encode the local DB
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    commit_msg = f"Updated {url.rsplit('/', 1)[-1]}"
    # Prepare PUT payload
    payload = {
        "message": commit_msg,
        "content": encoded,
        "sha": sha,
        "branch": "master"
    }

    put_resp = requests.put(url, headers=headers, data=json.dumps(payload), timeout=10)
    put_resp.raise_for_status()
    print("Database updated in GitHub.")
