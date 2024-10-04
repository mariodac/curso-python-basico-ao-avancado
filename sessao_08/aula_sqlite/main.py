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

# cria tabela
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
)
connection.commit()

# registrar valores nas colunas da tabela
# CUIDADO: sql injection
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (name, weight) VALUES ("Mario", 89.1), ("Douglas", 79.4)'
)
connection.commit()

# CUIDADO: fazendo DELETE sem WHERE
cursor.execute(f"DELETE FROM {TABLE_NAME}")
connection.commit()

# Redefine os id's
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
connection.commit()

cursor.execute(f'INSERT INTO {TABLE_NAME} (name, weight) VALUES ("Mario", 89.1)')
connection.commit()

cursor.close()
connection.close()
