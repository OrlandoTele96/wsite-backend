import logging
from Post import *
import datetime

class Blog:
    def __init__(self,db_cursor):
        self.db_cursor = db_cursor
        self.post_count = 0
        self.post_published = []
        self.post_hided = []
        self.posts = []
        self.last_published=[]
    
    def getPosts (self):
        #print ("This method query for table posts list")
        if self.db_cursor != None:
            self.db_cursor.execute('SELECT * FROM blog.posts')
            posts = self.db_cursor.fetchall()
            #print(posts)
            for p in posts:
                #print(type(p))
                post = Post(p)
                self.posts.append(post.convertToDict())
        



    def getPostCount(self):
        #print ("This method query for posts counting")
        if self.db_cursor != None:
            self.db_cursor.execute('SELECT count(*) FROM blog.posts')
            self.post_count=self.db_cursor.fetchone()[0]
            return self.post_count


    def getPostPublished(self):
        #print ("This method query for table posts pubished list")
        if self.db_cursor != None:
            self.db_cursor.execute('SELECT * FROM blog.posts WHERE is_posted = true')
            self.post_published=self.db_cursor.fetchall()

    def getCountPostPublisehd(self):
        return len(self.post_published)


    def getPostHiden(self):
        #print ("This method query for table posts hiden list")
        if self.db_cursor != None:
            self.db_cursor.execute('SELECT * FROM blog.posts WHERE is_posted = false')
            self.post_hided=self.db_cursor.fetchall()

    def getCountPostHidden(self):
        return len(self.post_hided)

    def getLasPostPublisehd(self):
        #print("Getting posts")
        if self.db_cursor != None:
            self.db_cursor.execute('SELECT DISTINCT ON ("post_id") * from blog.posts WHERE is_posted = true ORDER BY "post_id", "posted_date" DESC NULLS LAST, "post_title"')
            published=self.db_cursor.fetchall()
            count_post_publisehd=len(published)
            self.last_published=Post(published[count_post_publisehd-1])
            return self.last_published.convertToDict()
            

            

    def getAllPosts(self):
        return self.posts

    def getPublished(self):
        return self.post_published

    def sortPosts(self):
        pass

    def addPostInBlog(self,post,conn):
        #print ("Updating DB...")
        if self.db_cursor != None:
            try:
                self.db_cursor.execute("INSERT INTO blog.posts (post_id, post_title, image_id, content, posted_date, is_posted, is_image) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                (post['post_id'],post['post_title'],post['post_image_id'],post['post_content'],post['posted_date'],post['is_posted'],post['is_image']))
                conn.commit()
                #print ("Blog updated !!")
                status_code=200
            except Exception as ex:
                #print("DB could not be updated")
                status_code=500
            finally:
                return status_code

    def getBlogInfo(self):
        #print("Get blog information")
        self.bloginfo={}
        self.bloginfo['count-posts']=self.getPostCount()
        self.bloginfo['last-post-published']=self.getLasPostPublisehd()
        self.bloginfo['count-posts-published']=self.getCountPostPublisehd()
        self.bloginfo['count-posts-hidden']=self.getCountPostHidden()
        return self.bloginfo






