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

    with connection.cursor() as cursor:
        result = cursor.execute(
            f"INSERT INTO {TABLE_NAME} (nome, idade) VALUES ('Mario', 29)"
        )
        print(result)
    connection.commit()
