#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Expense Tracker Application
A command-line application to track expenses, view them, and generate statistics.
"""

# import logging

# internal imports
import ops
import stats
import user_input as ui
from github import download_from_github, upload_to_github
from config import DB_LOCAL_PATH
import db_handler


def main():
    """
    Main function to run the spend tracker application.
    """
    download_from_github("db")
    db_handler.create_table(DB_LOCAL_PATH)
    while True:
        print("\nExpense Tracker - Choose an option:")
        print("1. Add expense")
        print("2. Delete expense")
        print("3. View expenses")
        print("4. View statistics")
        print("5. Exit")
        choice = input("Enter your choice (1-5): \n").strip()

        if choice == "1":
            ops.add_expense()
            upload_to_github("db")
        elif choice == "2":
            ops.delete_expense()
            upload_to_github("db")
        elif choice == "3":
            ops.view_expenses()
        elif choice == "4":
            stats.generate_monthly_summary("June", 2025)
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
