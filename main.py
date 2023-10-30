from fastapi import FastAPI
from model import Post

# Create app object
app = FastAPI()


@app.get("/")
def root():
    return {"message": "welcome to my api!!!!!"}


@app.get("/posts")
def get_posts():
    return {"data": "A List of posts"}


@app.post("/create")
def create_posts(new_post: Post):
    print(new_post.model_dump())
    return new_post
