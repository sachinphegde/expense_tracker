"""
A simple command-line spend tracker application.
"""

import sqlite3
import datetime
import calendar

# internal imports
from config import DB_PATH


def add_expense():
    """
    Adds a new expense to the database.
    """
    expense_date = input("Enter date (dd-mm-yyyy) or press Enter for today: ").strip()
    if not expense_date:
        expense_date = datetime.datetime.now().strftime("%d-%m-%Y")
    print(f"adding expense for {expense_date}. Enter q to quit.")
    ex_day, ex_month, ex_year = expense_date.split('-')
    ex_month = calendar.month_name[int(ex_month)]

    while True:
        while True:
            amount = input("Amount (or 'q' to quit): ").strip()
            if amount == 'q':
                print("Exiting expense addition.")
                return
            try:
                amount_value = float(amount)
                break
            except ValueError:
                print("Please enter a valid number for amount.")
        description = input("Description: ").strip()
        category = input("Category: ").strip()
        sub_category = input("Sub Category: ").strip()
        if not amount or not category:
            print("Amount and category are required.")
            continue
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO expenses (
            description, amount, category, subCategory, date, month, year)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (description, amount_value, category, sub_category, expense_date, ex_month, ex_year)
        )
        conn.commit()
        conn.close()
        print("Expsense added.\n")


def delete_expense(args):
    """
    Deletes an expense from the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM expenses WHERE id = ?
        """,
        (args.id,))
    expense = cursor.fetchone()
    print(f"ID: {expense[0]}, Description: {expense[1]}, Amount: {expense[2]}, Category: {expense[3]}, SubCategory: {expense[4]}, Date: {expense[5]}")
    if expense:
        print(f"Deleting expense: {expense}")
        cursor.execute("""
                DELETE FROM expenses where id = ?
                """, (args.id,))
        print("Expense deleted.")
    else:
        print("Expense not found.")
    conn.commit()
    conn.close()


def view_expenses():
    """
    Reads the expenses table from the SQLite database and prints it as a table in the CLI.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, amount, category, date, description, month, year FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No expenses found.")
        return

    # Print header
    headers = ["ID", "Amount", "Category", "Date", "Description", "Month", "Year"]
    print("{:<5} {:<10} {:<15} {:<12} {:<23} {:<10} {:<6}".format(*headers))
    print("-" * 100)
    for row in rows:
        print("{:<5} {:<10} {:<15} {:<12} {:<23} {:<10} {:<6}".format(*[str(col) for col in row]))
