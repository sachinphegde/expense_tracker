"""
database_handler.py
This module provides functions to manage the expenses database
"""

import sqlite3
import requests
import base64
import json
from dotenv import load_dotenv
import os


def create_database(db_name):
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


def download_db_from_github(token, out_file="expenses.db"):
    url = DATABASE_URL
    headers = {"Authorization": f"token {token}"}
    r = requests.get(url, headers=headers)
    r.raise_for_status()

    download_url = r.json()["download_url"]
    db_content = requests.get(download_url)
    with open(out_file, "wb") as f:
        f.write(db_content.content)

    print(f"Downloaded database to {out_file}")


def upload_db_to_github(token, local_file="expenses.db", commit_msg="Update DB"):
    # Get SHA of existing file
    url = DATABASE_URL
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(get_url, headers=headers)
    resp.raise_for_status()

    sha = resp.json()["sha"]

    # Read and base64 encode the local DB
    with open(local_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    # Prepare PUT payload
    payload = {
        "message": commit_msg,
        "content": encoded,
        "sha": sha,
        "branch": "master"
    }

    put_resp = requests.put(get_url, headers=headers, data=json.dumps(payload))
    put_resp.raise_for_status()
    print("Database updated in GitHub.")


def get_github_token():
    load_dotenv()  # Load .env into environment
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    if not GITHUB_TOKEN:
        raise ValueError("GitHub token not found in .env file!")
