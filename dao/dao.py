import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


class PostDao:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

    def get_posts(self):
        cursor = self.connection.cursor()
        query = "SELECT id, title, content, published, created_date FROM posts;"
        cursor.execute(query)

        # convert list into json
        columns = [column[0] for column in cursor.description]
        posts = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return posts



