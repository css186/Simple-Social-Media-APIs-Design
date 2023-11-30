import json

from fastapi import FastAPI, Response, status, HTTPException
from model.Post import Post
from service.service import PostService

# Create app object
app = FastAPI()

# create service object
post_service = PostService()


@app.get("/")
def root():
    return {"message": "welcome to my api!!!!!"}


@app.get("/posts")
def get_posts():
    posts = post_service.get_posts()
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(new_post: Post):
    new_post = new_post.model_dump()
    title = new_post.get("title")
    content = new_post.get("content")
    published = new_post.get("published")
    post_service.create_post(title, content, published)
    return new_post

@app.get("/posts/{id}")
def get_post(id: int, response: Response):

    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found"
        )
    return {"post_detail": f"{post}"}


@app.delete("/posts/{id}")
def delete_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    return {"message": "updated post"}



def find_post(id):
    pass