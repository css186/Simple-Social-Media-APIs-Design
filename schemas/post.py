from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CreatePostRequest(BaseModel):
    title: str
    content: str
    published: bool = True

class PostResponse(BaseModel):
    title: str
    content: str
    published: bool = True
    created_at: Optional[datetime]
