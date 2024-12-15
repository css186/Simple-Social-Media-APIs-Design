from fastapi import HTTPException
import psycopg
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from database import get_connection
import logging

class PostModel:
    @staticmethod
    def get_posts():
        try:
            with get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM posts")
                    posts = cursor.fetchall()
                    return posts
        except Exception as e:
            logging.error(f"Error fetching posts: {e}")
            raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")