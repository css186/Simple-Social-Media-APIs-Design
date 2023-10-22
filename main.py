from fastapi import FastAPI

# Create app object
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
