from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # give default value
    # rating: Optional[int] = None

