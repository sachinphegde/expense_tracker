import re


def extract_inline_fields(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(content)
        # Match lines with the format Key:: Value
        fields = re.findall(r'^\s*([\w\s]+)::\s*(.+?)\s*$', content, re.MULTILINE)

        # Convert to dictionary
        field_dict = {key.strip(): value.strip() for key, value in fields}
        return field_dict
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"IO error opening file: {e}")



def extract_items_with_dates(file_path):
    """
    Extracts list items and their associated dates from a markdown file,
    ignoring content inside code blocks (e.g., ```dataviewjs ... ```).

    Returns a list of dictionaries with 'date' and 'item' keys.
    """
    items = []
    in_code_block = False
    current_date = None

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Detect start/end of code block
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue

            # Detect date header
            date_match = re.match(r"^##\s+(.+)", line)
            if date_match:
                current_date = date_match.group(1).strip()
                continue

            # Detect list item
            item_match = re.match(r"^- (.+)", line)
            if item_match and current_date:
                items.append({
                    "date": current_date,
                    "item": item_match.group(1).strip()
                })

    return items


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
    icloud_path_1 = os.path.join(
        "~",
        "Library",
        "Mobile Documents",
        "iCloud~md~obsidian",
        "Documents",
        "FinancePlans",
        "2025",
        "budget-2025.md"
    )

    icloud_path = os.path.join(
        "~",
        "Library",
        "Mobile Documents",
        "iCloud~md~obsidian",
        "Documents",
        "FinancePlans",
        "2025",
        "Spendings",
        "May.md"
    )
    full_path = os.path.expanduser(icloud_path)
    if not os.path.exists(full_path):
        print("File does not exist.")
        return
    fields = pm.extract_items_with_dates(full_path)
    print(fields)


if __name__ == "__main__":
    main()