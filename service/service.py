from dao.dao import PostDao


class PostService:
    def __init__(self):
        self.post_dao = PostDao()

    def get_posts(self):
        return self.post_dao.get_posts()

