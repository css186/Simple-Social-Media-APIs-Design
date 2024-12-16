from fastapi import FastAPI, Response, HTTPException, status
import psycopg
import os
from dotenv import load_dotenv
from schemas import Post


# Create an instance of FastAPI
app = FastAPI()


# Just for demonstration purposes (temporary)
load_dotenv()

HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")


conn = psycopg.connect(f"dbname={DB} user={USER}")
cur = conn.cursor()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    cur.execute("""SELECT * FROM posts""")
    posts = cur.fetchall()
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    sql = """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """
    cur.execute(sql, (post.title, post.content, post.published))
    new_post = cur.fetchone()
    conn.commit()
    return {
        "message": "Post created successfully",
        "details": new_post
    }

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    sql = """SELECT * FROM posts WHERE id = %s"""
    cur.execute(sql, (post_id,)) # Note that the second argument must be a tuple
    post = cur.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")
    return {"data": post}

@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    sql = """DELETE FROM posts WHERE id = %s RETURNING *"""
    cur.execute(sql, (post_id,))
    deleted_post = cur.fetchone()
    conn.commit()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")
    return {"message": "Post deleted successfully", "details": deleted_post}

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    sql = """UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *"""
    cur.execute(sql, (post.title, post.content, post.published, post_id))
    updated_post = cur.fetchone()
    conn.commit()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")
    return {"message": "Post updated successfully", "details": updated_post}