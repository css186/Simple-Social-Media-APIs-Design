from fastapi import FastAPI
from fastapi.params import Body

# Create app object
app = FastAPI()


@app.get("/")
def root():
    return {"message": "welcome to my api!!!!!"}


@app.get("/posts")
def get_posts():
    return {"data": "A List of posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    return {"new_post": f"title {payload['title']}, content: {payload['content']}"}
