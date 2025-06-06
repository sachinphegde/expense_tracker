#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Expense Tracker Application
A command-line application to track expenses, view them, and generate statistics.
"""

import os
import sys

# internal imports
import db_handler
import ops
import user_input as ui

from config import EXPENSE_DB
from db_handler import download_db_from_github, upload_db_to_github


def main():
    """
    Main function to run the spend tracker application.
    """
    download_db_from_github()
    if not os.path.exists(EXPENSE_DB):
        db_handler.create_database(EXPENSE_DB)

    try:
        args = ui.get_user_args()
    except SystemExit as error:
        sys.exit(error.code)

    if args.command == "add":
        ops.add_expense()
    elif args.command == "delete":
        ops.delete_expense(args)
    elif args.command == "view":
        ops.view_expenses()

    upload_db_to_github(EXPENSE_DB)


if __name__ == "__main__":
    main()
