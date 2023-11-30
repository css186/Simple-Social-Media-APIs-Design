from fastapi import FastAPI
from model.Post import Post

# Create app object
app = FastAPI()


@app.get("/")
def root():
    return {"message": "welcome to my api!!!!!"}


@app.get("/posts")
def get_posts():
    return {"data": "A List of posts"}


@app.post("/posts")
def create_posts(new_post: Post):
    result = new_post.model_dump()
    print(result)
    print(type(result))
    return new_post


@app.get("/posts/{id}")
def get_post(id: int):
    print(id)
    return id
