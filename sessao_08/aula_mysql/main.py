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
        print(cursor)
