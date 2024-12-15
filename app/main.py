from fastapi import FastAPI, Response, HTTPException, status
from model.post import Post

# Create an instance of FastAPI
app = FastAPI()


# Create a list to store the posts
my_posts = []

def find_post(post_id):
    for p in my_posts:
        if p["id"] == post_id:
            return p
    return None


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.get("/posts/latest")
def get_latest_post():
    return my_posts[-1]


# Get single post
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in my_posts:
        if post["id"] == post_id:
            return {"message": "Post found", "data": post}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {post_id} was not found"
    )

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = len(my_posts) + 1
    my_posts.append(post_dict)
    return {"message": "Post created successfully", "data": post_dict}

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {post_id} was not found"
        )
    my_posts.remove(post)
    return

# Update
@app.put("/posts/{post_id}")
def update_post(post_id: int, new_post: Post):
    post = find_post(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {post_id} was not found"
        )
    post.update(new_post)
    return {"message": "Post updated successfully", "data": post}
