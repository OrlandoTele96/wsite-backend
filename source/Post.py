import logging

class Post:
    def __init__(self, posts):
        self.post_id= posts[0]
        self.post_title=posts[1]
        self.post_image_id=posts[2]
        self.post_content=posts[3]
        self.posted_date=posts[4]
        self.is_posted= posts[5]
        self.is_image = posts[6]
        #self.post_dict = {}
    def convertToDict(self):
        post_dict = self.__dict__
        return post_dict

