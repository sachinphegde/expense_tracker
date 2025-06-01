"""
Statistics module for the Expense Tracker application.
This module provides functions to generate statistics or graphs based on the expenses.
"""

import matplotlib.pyplot as plt
import sqlite3


def generate_statistics():
    """_summary_
    """
    print("Generating statistics...")


def get_expense_sum():
    """
    Calculates the total sum of expenses in the database.
    """
    conn = sqlite3.connect(EXPENSE_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_sum = cursor.fetchone()[0]
    conn.close()
    return total_sum if total_sum is not None else 0.0