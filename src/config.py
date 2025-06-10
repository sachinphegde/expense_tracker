"""
config file for the expense tracker application
database path and other configurations
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Load .env once, when this module is imported

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
DB_PATH = os.getenv("DB_PATH")
