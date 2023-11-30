import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Establishing a connection to the MySQL database
# try:
connection = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

cursor = connection.cursor()

query = "SELECT * FROM posts"

cursor.execute(query)

columns = [column[0] for column in cursor.description]
data = [dict(zip(columns, row)) for row in cursor.fetchall()]

print(data)



# except mysql.connector.Error as e:
#     print(f"Error connecting to MySQL database: {e}")
#
# finally:
#     # Closing the connection
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
#         print("MySQL connection is closed")
