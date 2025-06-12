"""
Statistics module for the Expense Tracker application.
This module provides functions to generate statistics or graphs based on the expenses.
"""

import matplotlib.pyplot as plt
import sqlite3

from config import DB_PATH


def generate_statistics():
    """_summary_
    """
    print("Generating statistics...")


def get_expense_sum():
    """
    Calculates the total sum of expenses in the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_sum = cursor.fetchone()[0]
    conn.close()
    if total_sum is not None:
        print(f"Total expenses: {total_sum:.2f}")
    else:
        print("Total expenses: 0.00")
