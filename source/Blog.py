import logging
from Post import *

class Blog:
    def __init__(self,db_cursor):
        self.db_cursor = db_cursor
        self.post_count = 0
        self.post_published = []
        self.post_hided = []
        self.posts = []
    
    def getPosts (self):
        print ("This method query for table posts list")
        if self.db_cursor != None:
            self.db_cursor.execute('SELECT * FROM blog.posts')
            posts = self.db_cursor.fetchall()
            for p in posts:
                post = Post(p)
                self.posts.append(post.convertToDict())
            print (self.posts)


    def getPostCount(self):
        print ("This method query for posts counting")
        if self.db_cursor != None:
            self.db_cursor.execute('SELECT count(*) FROM blog.posts')
            self.post_count=self.db_cursor.fetchone()[0]


    def getPostPublished(self):
        print ("This method query for table posts pubished list")
        if self.db_cursor != None:
            self.db_cursor.execute('SELECT * FROM blog.posts WHERE is_posted = true')
            self.post_published=self.db_cursor.fetchall()


    def getPostHiden(self):
        print ("This method query for table posts hiden list")
        if self.db_cursor != None:
            self.db_cursor.execute('SELECT * FROM blog.posts WHERE is_posted = false')
            self.post_hided=self.db_cursor.fetchall()

    def getAllPosts(self):
        return self.posts

    def getPublished(self):
        return self.post_published

    def sortPosts(self):
        pass


