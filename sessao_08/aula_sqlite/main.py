import sqlite3
from pathlib import Path

# SQLite tutorial - https://www.techonthenet.com/sqlite/index.php
# SQLite Documentação - https://www.sqlite.org/doclist.html
# DBeaver CE - https://dbeaver.io/download/

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
)
connection.commit()

cursor.close()
connection.close()
