"""
Main script for accessing and reading a finance budget file stored in an iCloud-synced Obsidian vault.

This script attempts to locate and open a markdown file containing budget information for the year 2025.
It prints the contents of the file if found, or an error message if the file does not exist or cannot be opened.

Usage:
    python main.py
"""

import os

def main():
    """
    Attempts to open and read a budget markdown file from an iCloud-synced Obsidian vault.

    The function constructs the file path, checks for the file's existence, and prints its contents.
    If the file does not exist or cannot be opened, it prints an appropriate error message.
    """
    icloud_path = os.path.join(
        "~",
        "Library",
        "Mobile Documents",
        "iCloud~md~obsidian",
        "Documents",
        "FinancePlans",
        "2025",
        "budget-2025.md"
    )
    full_path = os.path.expanduser(icloud_path)
    print(f"Trying to open: {full_path}")
    if not os.path.exists(full_path):
        print("File does not exist.")
        return
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            data = f.read()
            print(data)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"IO error opening file: {e}")


if __name__ == "__main__":
    main()
