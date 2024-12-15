from typing import Optional
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    contents: str
    published: bool = True
    rating: Optional[int] = None
