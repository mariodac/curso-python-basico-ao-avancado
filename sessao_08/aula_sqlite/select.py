import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = 3")

# obtem todos os registros da consulta
for row in cursor.fetchall():
    _id, name, weigth = row
    print(_id, name, weigth)
# como retorna um iterator no código acima esgotou o iterator e no print está "None"
row = cursor.fetchone()
print(row)


cursor.close()
connection.close()
