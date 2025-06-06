import os
import sys
import subprocess
import venv
from pathlib import Path


VENV_DIR = Path(venv)


def create_virtualenv():
    """Create a virtual environment."""
    if not VENV_DIR.exists():
        print(f"Creating virtual environment at {VENV_DIR}")
        venv.create(VENV_DIR, with_pip=True)
    else:
        print(f"Virtual environment already exists at {VENV_DIR}")


def install_requirements():
    """Install requirements from requirements.txt."""
