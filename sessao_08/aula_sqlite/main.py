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

# CRUD - Create Read Update Delete
# SQL- INSERT SELECT UPDATE DELETE

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

# maneira de evitar o sql injection, os valores serão passados como parametros
# na função e não diretamente na string
# esses paramentros são listas, tuplas, dicionarios
sql = f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)"
sql_dict = f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (:nome, :peso)"
# executando com lista de valores
cursor.execute(sql, ["Janaina", 82.1])
# executando com tupla de valores
cursor.execute(sql, ("Joana", 85.1))
# executando com dicionario
cursor.execute(sql_dict, {"nome": "Jose", "peso": 45.5})
# executando varios com uma lista de listas de valores
cursor.executemany(sql, [["João", 81.1], ["Mario", 89.1], ["Luiz", 75.1]])
# executando varios com uma tupla de iteráveis(lista/tupla) de valores
cursor.executemany(sql, (("Ricardo", 83.1), ["Jonas", 99.1], ("Vitor", 57.1)))
# executando varios com uma lista de dicionarios
cursor.executemany(
    sql_dict,
    [
        {"nome": "Lucas", "peso": 78.1},
        {"nome": "Mateus", "peso": 63.1},
        {"nome": "Carlos", "peso": 92.1},
    ],
)
# executando varios com uma tupla de dicionarios
cursor.executemany(
    sql_dict,
    (
        {"nome": "Judas", "peso": 77.1},
        {"nome": "Josue", "peso": 65.1},
        {"nome": "Henrique", "peso": 91.1},
    ),
)
connection.commit()

cursor.close()
connection.close()
