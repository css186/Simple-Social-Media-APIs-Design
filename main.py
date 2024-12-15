from fastapi import FastAPI, Body
from model.post import Post

# Create an instance of FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "list of posts"}


@app.post("/posts")
def create_post(new_post: Post):
    return new_post.model_dump()