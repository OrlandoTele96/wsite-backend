from DBConnect import *
from ConfigParserDB import *
from Blog import *
import flask
import jsonify

if __name__ == "__main__":
    print ("Backend stating...")
    print ("Loading configurations")
    file_config = "/Users/jorgeorlandogonzalezguzman/Documents/Projects/website/wsite-backend/source/postgres.ini"
    section_config="postgresql"
    config_db_parser = ConfigParserDB(file_config,section_config)
    db_config=config_db_parser.getConfig()
    blog_db = DBConnect(db_config)
    db_cursor=blog_db.Connect()
    print("Getting DB information")
    blog = Blog(db_cursor)
    blog.getPostCount()
    blog.getPostPublished()
    blog.getPosts()
    
    blog_db.DBDisconnect(db_cursor)
