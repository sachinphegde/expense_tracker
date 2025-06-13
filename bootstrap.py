"""
bootstrap.py
This script sets up a virtual environment and installs the required packages
for the project.
It is designed to be run in a Python 3.6+ environment.
"""

import os
import sys
import subprocess
import venv
from pathlib import Path

VENV_DIR = Path("venv")


def create_virtualenv():
    """Create a virtual environment."""
    if not VENV_DIR.exists():
        print(f"Creating virtual environment at {VENV_DIR}")
        venv.create(VENV_DIR, with_pip=True)
    else:
        print(f"Virtual environment already exists at {VENV_DIR}")


def install_requirements():
    """Install requirements from requirements.txt."""
    python_exe = VENV_DIR / "Scripts" / "python.exe" if os.name == "nt" else VENV_DIR / "bin" / "python"
    subprocess.run(
        [str(python_exe), "-m", "pip", "install", "-r", "requirements.txt"],
        check=True,
    )


def main():
    """Main function to set up the virtual environment and install requirements."""
    create_virtualenv()
    install_requirements()
    print("Virtual environment setup complete.")


if __name__ == "__main__":
    if sys.version_info < (3, 6):
        print("Python 3.6 or higher is required.")
        sys.exit(1)

    main()
    print("Running bootstrap script...")
