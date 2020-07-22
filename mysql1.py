import pymysql
import json
from datetime import datetime
import config




def runCommand(command):
    dbconn = connect()#will connect to the mysql db
    co = dbconn.cursor()# following will send command to the database and get a response
    co.execute(command)
    s = list()
    for result in co.fetchall():# will take all the results from the command and create a list to return back
        s.append(result)
    dbconn.commit ()# commit connection
    dbconn.close()#end connection
    return s


def connect():
    try:
        mydb = pymysql.connect(host=config.dbhost,# grabs credentials from config file 
                               user=config.dbuser,
                               password=config.dbpass,
                               db=config.dbname,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        return mydb
    except:
        print("error connecting to database")
        return None


