from dotenv import load_dotenv
from psycopg_pool import ConnectionPool
import os

load_dotenv()

HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

# Create a connection pool
DB_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

try:
    pool = ConnectionPool(DB_URL)
except Exception as e:
    print(f"Error creating connection pool: {e}")
    pool = None

def get_connection():
    if pool is None:
        raise Exception("Connection pool is not available")
    return pool.connection()

def close_pool():
    if pool is not None:
        pool.close()