from audioop import add
import psycopg2

class DBConnect:
    def __init__(self,db_config):
        print("Connection DB class is initializing...")
        self.db_config=db_config

    def Connect(self):
        print ("Starting connection with postgresql db...")
        conn=None
        try:
            print("Trying to connect with DB server : \t",self.db_config['host'])
            conn = psycopg2.connect(**self.db_config)
            cur = conn.cursor()
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')
            db_version = cur.fetchone()
            print(db_version)
            #self.getTable(cur)
            #db_posts = cur.fetchone()
            #print(db_posts, type(db_posts))
        except (Exception, psycopg2.DatabaseError) as Error:
            print(Error)
        finally:
            if conn is not None:
                print ("DB conection is successful")
                return cur
            #    conn.close()
            #    print("DB connection closed...")

    def getTable(self,cursor):
        print ("This method query for table posts list")
        if cursor != None:
            cursor.execute('SELECT * FROM blog.posts')

    def DBDisconnect(self,db_cursor):
        if db_cursor is not None:
            db_cursor.close()
            print("Conection DB is closed")


    



    