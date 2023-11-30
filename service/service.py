from dao.dao import PostDao


class PostService:
    def __init__(self):
        self.post_dao = PostDao()

    def get_posts(self):
        return self.post_dao.get_posts()

    def create_post(self, title, content, published):
        self.post_dao.create_post(title, content, published)

    def get_post(self, id):
        return self.post_dao.get_post(id)
