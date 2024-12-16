from typing import List
from fastapi import FastAPI, HTTPException, status, Depends
from schemas import PostCreate, PostResponse
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine, conn, cur, get_db, Base

# Create an instance of FastAPI
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    # cur.execute("""SELECT * FROM posts""")
    # posts = cur.fetchall()
    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump()) # unpack the post object and create a new Post object
    db.add(new_post) # stage the new post
    db.commit() # commit the new post to the database
    db.refresh(new_post) # retrieve the new post and return it
    # sql = """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """
    # cur.execute(sql, (post.title, post.content, post.published))
    # new_post = cur.fetchone()
    # conn.commit()
    return new_post

@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first() #.first() is more efficient than .all()
    # sql = """SELECT * FROM posts WHERE id = %s"""
    # cur.execute(sql, (post_id,)) # Note that the second argument must be a tuple
    # post = cur.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")
    return post

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter(models.Post.id == post_id)
    deleted_post = query.first()
    # sql = """DELETE FROM posts WHERE id = %s RETURNING *"""
    # cur.execute(sql, (post_id,))
    # deleted_post = cur.fetchone()
    # conn.commit()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")
    query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Post deleted successfully", "details": deleted_post}

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    query = db.query(models.Post).filter(models.Post.id == post_id)
    updated_post = query.first()
    # sql = """UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *"""
    # cur.execute(sql, (post.title, post.content, post.published, post_id))
    # updated_post = cur.fetchone()
    # conn.commit()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} not found")

    query.update(post.model_dump(), synchronize_session=False)
    db.commit()
    return updated_post