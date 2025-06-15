"""
database_handler.py
This module provides functions to manage the expenses database
"""

import sqlite3


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
