import pymysql
import json
from datetime import datetime
import config1




def runCommand(command):
    dbconn = connect()
    co = dbconn.cursor()
    co.execute(command)
    s = list()
    for result in co.fetchall():
        s.append(result)
    dbconn.commit ()
    dbconn.close()
    return s


def connect():
    try:
        mydb = pymysql.connect(host=config1.dbhost,
                               user=config1.dbuser,
                               password=config1.dbpass,
                               db=config1.dbname,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
        return mydb
    except:
        print("error connecting to database")
        return None


#runCommand("SELECT * FROM weather.today;")# test 