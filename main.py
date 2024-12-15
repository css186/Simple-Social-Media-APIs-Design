from fastapi import FastAPI, Body

# Create an instance of FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "list of posts"}


@app.post("/posts")
def create_post(payload: dict = Body(...)):
    return {
        "message": "Post has been created successfully",
        "new_post_title": payload["title"],
        "new_post_contents": payload["contents"]
    }
