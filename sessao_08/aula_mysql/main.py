import pymysql
import os
from dotenv import load_dotenv

TABLE_NAME = "users"

load_dotenv()

connection = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
)
# sem context manager
# cursor = connection.cursor()

# cursor.close()
# connection.close()


# com context manager
with connection:
    with connection.cursor() as cursor:
        # create table não precisa de commit
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INT NOT NULL AUTO_INCREMENT, nome VARCHAR(50) NOT NULL, idade INT NOT NULL, PRIMARY KEY (id))"
        )
        # CUIDADO este comando apaga todos os dados da tabela
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")
    connection.commit()

    # Inicio da manipulação dados a partir daqui

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)"
        # tupla é utilizado para quando não é necessário mudar os valores, ou seja, você está apenas passando os valores
        result = cursor.execute(sql, ("Mario", 29))
        result = cursor.execute(sql, ["Douglas", 30])
    # Chamada da função necessária sempre que modificar alguma tabela na base de dados
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%(name)s, %(age)s)"
        data = {"name": "João", "age": 29}
        result = cursor.execute(sql, data)
    connection.commit()

    # Inserindo um valor usando placeholders e uma tupla de dicionários
    with connection.cursor() as cursor:
        sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%(name)s, %(age)s)"
        data2 = (
            {"name": "Otavio", "age": 23},
            {"name": "Victor", "age": 25},
            {"name": "Rosa", "age": 50},
        )
        result = cursor.executemany(sql, data2)
    connection.commit()

    # Inserindo um valor usando placeholders e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql = f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)"
        data3 = (
            ("Geraldo", 13),
            ("Helio", 15),
            ("Julia", 60),
        )
        result = cursor.executemany(sql, data3)
        print(result)
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        id_less = input("Digite o menor id: ")
        id_greater = input("Digite o maior id: ")
        coluna = "id"
        sql = f"SELECT * FROM {TABLE_NAME} WHERE {coluna} >= %s AND {coluna} <= %s"
        cursor.execute(sql, (id_less, id_greater))
        print(cursor.mogrify(sql, (id_less, id_greater)))
        data4 = cursor.fetchall()
        for row in data4:
            print(row)
