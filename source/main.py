from DBConnect import *
from ConfigParserDB import *
from Blog import *
from flask import Flask, redirect, url_for, request
from flask import jsonify
import requests
import os
#import jsonify

file_config = os.environ['PWD']+"/postgres.ini"
section_config="postgresql"
config_db_parser = ConfigParserDB(file_config,section_config)

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/api/v1/users/', methods=['GET'])
def get_users():
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/posts/',methods=['GET','POST'])
def getPosts():
    #posts = [{'post_id':1, 'post_content': "Hello world"},
    #{'post_id':2, 'post_content': "Hello world x2"}]
    db_config=config_db_parser.getConfig()
    blog_db = DBConnect(db_config)
    db_cursor=blog_db.Connect()
    #print("Getting DB information")
    blog = Blog(db_cursor)
    if request.method == 'GET':
        blog.getPosts()
        posts= blog.getAllPosts()
        blog_db.DBDisconnect(db_cursor)
        return jsonify({'posts': posts})
    if request.method == 'POST':
        try:
            post= request.json
            conn=blog_db.getConnection()
            status=blog.addPostInBlog(post,conn)
            blog_db.DBDisconnect(db_cursor)
        except Exception as ex: 
            return jsonify({"message":"ERROR"}), 500
        finally:
            if status==200:
                return jsonify({"message":"Success"}), 200
            else:
                return jsonify({"message":"ERROR"}), 500


@app.route('/post/<post_id>',methods=['GET','POST'])
def getPostbyId(post_id):
    db_config=config_db_parser.getConfig()
    blog_db = DBConnect(db_config)
    db_cursor=blog_db.Connect()
    #print("Getting DB information")
    blog = Blog(db_cursor)
    if request.method == 'GET':
        blog.getPosts()
        posts= blog.getAllPosts()
        blog_db.DBDisconnect(db_cursor)
        #post = [p for p in posts if p["post_id"] == post_id]
        postid=int(post_id)
        """for p in posts:
            if p["post_id"] == postid:
                #print (p)"""
        post={"post":p for p in posts if p["post_id"]== postid}
        if not post:
            #print ("Dictionary is empty")
            return jsonify({"post": "Post doesn't exist"}), 404
        return jsonify(post)
    else:
        return jsonify({"post": "Bad request"}), 400

@app.route('/blog/info',methods=['GET'])
def getBlogInformation():
    db_config=config_db_parser.getConfig()
    blog_db = DBConnect(db_config)
    db_cursor=blog_db.Connect()
    #print("Getting DB information")
    blog = Blog(db_cursor)
    if request.method=='GET':
        blog.getPosts()
        blog.getPostPublished()
        blog.getPostHiden()
        """
        1.- N. posts
        2.- Last posts title/ID
        3.- N. Posts published
        4.- N. posts hidden
        """
        info=blog.getBlogInfo()
        return (info), 200




if __name__ == "__main__":
    #print ("Backend starting...")
    #print ("Loading configurations")    
    app.run(host="192.168.100.11",port="5000",debug=True)