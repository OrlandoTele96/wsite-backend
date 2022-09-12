from DBConnect import *
from ConfigParserDB import *
from Blog import *
from flask import Flask
from flask import jsonify
#import jsonify

file_config = "/Users/jorgeorlandogonzalezguzman/Documents/Projects/website/wsite-backend/source/postgres.ini"
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

@app.route('/posts/',methods=['GET'])
def getPosts():
    #posts = [{'post_id':1, 'post_content': "Hello world"},
    #{'post_id':2, 'post_content': "Hello world x2"}]
    db_config=config_db_parser.getConfig()
    blog_db = DBConnect(db_config)
    db_cursor=blog_db.Connect()
    print("Getting DB information")
    blog = Blog(db_cursor)
    blog.getPosts()
    posts= blog.getAllPosts()
    blog_db.DBDisconnect(db_cursor)
    return jsonify({'posts': posts})


@app.route('/post/<post_id>',methods=['GET'])
def getPostbyId(post_id):
    db_config=config_db_parser.getConfig()
    blog_db = DBConnect(db_config)
    db_cursor=blog_db.Connect()
    print("Getting DB information")
    blog = Blog(db_cursor)
    blog.getPosts()
    posts= blog.getAllPosts()
    blog_db.DBDisconnect(db_cursor)
    #post = [p for p in posts if p["post_id"] == post_id]
    postid=int(post_id)
    """for p in posts:
        if p["post_id"] == postid:
            print (p)"""
    post={"post":p for p in posts if p["post_id"]== postid}
    if not post:
        print ("Dictionary is empty")
        return jsonify({"post": "Post doesn't exist"}), 404
    return jsonify(post)

if __name__ == "__main__":
    print ("Backend starting...")
    print ("Loading configurations")    
    app.run(host="192.168.100.11",port="5000",debug=True)
