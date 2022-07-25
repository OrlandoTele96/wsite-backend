from DBConnect import *
from ConfigParserDB import *

if __name__ == "__main__":
    print ("Backend stating...")
    print ("Loading configurations")
    file_config = "/Users/jorgeorlandogonzalezguzman/Documents/Projects/website/wsite-backend/source/postgres.ini"
    section_config="postgresql"
    config_db_parser = ConfigParserDB(file_config,section_config)
    db_config=config_db_parser.getConfig()
    blog_db = DBConnect(db_config)
    blog_db.Connect()