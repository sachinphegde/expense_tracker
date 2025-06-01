"""
Expense Tracker Application
A command-line application to track expenses, view them, and generate statistics.
"""

import os
import sys
from pathlib import Path

# internal imports
import db_handler
import tracker
import user_input as ui

# Constants
# OS	| Path.home() points to
# ------|----------------------
# Linux	| /home/username
# macOS	| /Users/username
# Windows | C:\Users\username
homedir = Path.home()
EXPENSE_DB = homedir/"expenses.db"


def main():
    """
    Main function to run the spend tracker application.
    """
    if not os.path.exists(EXPENSE_DB):
        db_handler.create_database(EXPENSE_DB)

    try:
        args = ui.get_user_args()
    except SystemExit as error:
        sys.exit(error.code)

    if args.command == "add":
        tracker.add_expense()
    elif args.command == "view":
        tracker.view_expenses(args)
    elif args.command == "stats":
        tracker.stats_graph(args)


if __name__ == "__main__":
    main()
