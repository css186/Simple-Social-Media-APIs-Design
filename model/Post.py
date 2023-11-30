from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True  # give default value
    created_date: str
    # rating: Optional[int] = None
