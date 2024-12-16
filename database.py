from dotenv import load_dotenv
import os
# Native PostgreSQL connection
import psycopg

# SQLAlchemy related imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import models

load_dotenv()

HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

# Create a database URL
DB_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"


# Native PostgreSQL connection
conn = psycopg.connect(f"dbname={DB} user={USER}")
cur = conn.cursor()

# SQLAlchemy connection
# Handle database connections using SQLAlchemy
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

