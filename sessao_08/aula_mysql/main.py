import pymysql
import os
from dotenv import load_dotenv

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
            "CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT, nome VARCHAR(50) NOT NULL, idade INT NOT NULL, PRIMARY KEY (id))"
        )
        connection.commit()
