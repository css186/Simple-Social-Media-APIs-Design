from models.post_model import PostModel
from schemas.post import CreatePostRequest, PostResponse

class PostController:

    @staticmethod
    def get_posts() -> list[PostResponse]:
        posts = PostModel.get_posts() # return a python dictionary
        return [PostResponse(**post) for post in posts]