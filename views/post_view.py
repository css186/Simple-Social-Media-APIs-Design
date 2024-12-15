from fastapi import APIRouter, HTTPException, status
from schemas.post import CreatePostRequest, PostResponse
from Controllers.post_controller import PostController

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", response_model=list[PostResponse])
def get_posts():
    return PostController.get_posts()