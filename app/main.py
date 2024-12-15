from fastapi import FastAPI, Response, HTTPException, status
from views.post_view import router as post_router
import psycopg
import os
from dotenv import load_dotenv

# Create an instance of FastAPI
app = FastAPI()

# Include Routers
app.include_router(post_router)

@app.get("/")
def root():
    return {"message": "Hello World"}
