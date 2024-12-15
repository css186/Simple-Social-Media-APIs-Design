from models.post_model import PostModel
from schemas.post import CreatePostRequest, PostResponse

class PostController:

    @staticmethod
    def get_posts() -> list[PostResponse]:
        posts = PostModel.get_posts()
        return [
            PostResponse(
                id=post[0],
                title=post[1],
                content=post[2],
                published=post[3],
                created_at=post[4]) for post in posts]