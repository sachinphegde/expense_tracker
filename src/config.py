"""
config file for the expense tracker application
database path and other configurations
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Load .env once, when this module is imported

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
DB_LOCAL_PATH = os.getenv("DB_LOCAL_PATH")
BUDGET_URL = os.getenv("BUDGET_URL")
BUDGET_LOCAL_PATH = os.getenv("BUDGET_LOCAL_PATH")
