class PrankCallCommunity:
    def __init__(self):
        self.posts = []

    def create_post(self, post):
        self.posts.append(post)

    def get_posts(self):
        return self.posts