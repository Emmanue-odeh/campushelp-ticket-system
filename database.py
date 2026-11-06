import sqlite3
from pathlib import Path

DATABASE_DIR = Path(__file__).parent / "database"
DATABASE_PATH = DATABASE_DIR / "campushelp.db"


def get_connection():
    DATABASE_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection