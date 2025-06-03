"""
config file for the expense tracker application
database path and other configurations
"""


from pathlib import Path

# Constants
# OS	| Path.home() points to
# ------|----------------------
# Linux	| /home/username
# macOS	| /Users/username
# Windows | C:\Users\username
homedir = Path.home()
EXPENSE_DB = homedir / "expenses.db"

DATABASE_URL = "https://api.github.com/repos/sachinphegde/my_database/contents/Finance/expenses.db"
