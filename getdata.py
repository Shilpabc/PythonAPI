# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:56:02 2019

@author: Shilpa_Chikkannavar
"""

#!/usr/bin/python
import MySQLdb
import json
import pandas as pd

db = MySQLdb.connect(host="172.17.0.3",    # your host, usually localhost
                     user="demouser",         # your username
                     passwd="Welcome1!",  # your password
                     db="demodb")        # name of the data base
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM contDef")

def fetchData():
    
    df = pd.DataFrame()
    df = cur.fetchall();
    return df
# print all the first cell of all the rows
    
def list():
    for row in cur.fetchall():
        print (row[0] , row[1] , row[2])

db.close()


if __name__ == '__main__':
    df = fetchData()