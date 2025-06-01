#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple command-line spend tracker application.
"""
import argparse
import os
import sys
import sqlite3
import datetime
import calendar
from pathlib import Path
import matplotlib


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
        amount = input("Amount (or 'q' to quit): ").strip()
        if amount == 'q':
            break
        description = input("Description: ").strip()
        category = input("Category: ").strip()
        sub_category = input("Sub Category: ").strip()
        if not amount or not category:
            print("Amount and category are required.")
            continue
        conn = sqlite3.connect(EXPENSE_DB)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO expenses (
            description, amount, category, subCategory, date, month, year)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (description, float(amount), category, sub_category, expense_date, ex_month, ex_year)
        )
        conn.commit()
        conn.close()
        print("Expsense added.\n")


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


def view_expenses(args):
    """
    Views all expenses in the database.
    """
    conn = sqlite3.connect(EXPENSE_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE date = ?", (date_str,))

    conn.commit()
    conn.close()


def delete_expense(args):
    """
    Deletes an expense from the database.
    """
    conn = sqlite3.connect(EXPENSE_DB)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM expenses WHERE id = ?)
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


def stats_graph(args):
    """
    Generates statistics or a graph based on the expenses.
    """
    conn = sqlite3.connect(EXPENSE_DB)
    cursor = conn.cursor()

    conn.commit()
    conn.close()



