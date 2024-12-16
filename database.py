from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

# Create a database URL
DB_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"


