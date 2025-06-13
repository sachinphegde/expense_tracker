#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Expense Tracker Application
A command-line application to track expenses, view them, and generate statistics.
"""

import sys

# internal imports
import ops
import stats
import user_input as ui
from db_handler import download_db_from_github, upload_db_to_github


def main():
    """
    Main function to run the spend tracker application.
    """
    download_db_from_github()

    try:
        args = ui.get_user_args()
    except SystemExit as error:
        sys.exit(error.code)

    if args.command == "add":
        ops.add_expense()
        upload_db_to_github()
    elif args.command == "delete":
        ops.delete_expense(args)
        upload_db_to_github()
    elif args.command == "view":
        ops.view_expenses()
    elif args.command == "stats":
        stats.get_expense_sum()
        stats.get_expense_sum_by_category()


if __name__ == "__main__":
    main()
