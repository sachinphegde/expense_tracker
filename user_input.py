"""
input module for the expense tracker application.
"""
import argparse


def get_user_args():
    """
    Parses command-line arguments for the spend tracker application.
    """
    parser = argparse.ArgumentParser(description="A simple command-line spend tracker application.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Action to perform")

    # add_expense
    subparsers.add_parser('add', help='Add a new expense')

    # delete_expense
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('id', type=int, help='ID of the expense to delete')

    # view_expenses
    subparsers.add_parser('view', help='View all expenses')

    args = parser.parse_args()
    return args
