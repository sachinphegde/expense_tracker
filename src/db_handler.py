"""
database_handler.py
This module provides functions to manage the expenses database
"""

import sqlite3
import base64
import json
import requests
import os
from config import GITHUB_TOKEN, DATABASE_URL, DB_PATH


def create_table(db_name):
    """
    Creates the database and the expenses table if it does not exist.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            subCategory TEXT,
            date TEXT NOT NULL,
            month TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_column_to_expenses(db_name, column_name, column_type):
    """
    Adds a new column to the expenses table if it does not already exist.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    # Check if column already exists
    cursor.execute("PRAGMA table_info(expenses)")
    columns = [info[1] for info in cursor.fetchall()]
    if column_name not in columns:
        cursor.execute(f"ALTER TABLE expenses ADD COLUMN {column_name} {column_type}")
        print(f"Column '{column_name}' added.")
    else:
        print(f"Column '{column_name}' already exists.")
    conn.commit()
    conn.close()


def download_db_from_github():
    """
    Downloads the database from GitHub into the specified path.
    """

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(DATABASE_URL, headers=headers, timeout=10)
    r.raise_for_status()

    download_url = r.json()["download_url"]
    db_content = requests.get(download_url, timeout=10)
    with open(DB_PATH, "wb") as f:
        f.write(db_content.content)

    print(f"Downloaded database to {DB_PATH}")

    create_table(DB_PATH)


def upload_db_to_github(commit_msg="Update DB"):
    """
    Uploads the local database file to GitHub.

    Args:
        token (_type_): _description_
        local_file (str, optional): _description_. Defaults to "expenses.db".
        commit_msg (str, optional): _description_. Defaults to "Update DB".
    """
    # Get SHA of existing file
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    resp = requests.get(DATABASE_URL, headers=headers, timeout=10)
    resp.raise_for_status()

    sha = resp.json()["sha"]

    # Read and base64 encode the local DB
    with open(DB_PATH, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    # Prepare PUT payload
    payload = {
        "message": commit_msg,
        "content": encoded,
        "sha": sha,
        "branch": "master"
    }

    put_resp = requests.put(DATABASE_URL, headers=headers, data=json.dumps(payload), timeout=10)
    put_resp.raise_for_status()
    print("Database updated in GitHub.")
