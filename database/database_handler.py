"""
database_handler.py
This module provides functions to manage the expenses database
"""

import sqlite3


def add_column_to_expenses(column_name, column_type):
    """
    Adds a new column to the expenses table if it does not already exist.
    """
    conn = sqlite3.connect(EXPENSE_DB)
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