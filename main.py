from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

