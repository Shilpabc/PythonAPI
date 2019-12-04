# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 20:56:02 2019

@author: Shilpa_Chikkannavar
"""

#!/usr/bin/python
import MySQLdb
import json
import pandas as pd
import configparser

config = configparser.RawConfigParser()
config.read('ConfigFile.properties')

host=config.get('DatabaseSection', 'database.service')
user=config.get('DatabaseSection', 'database.user')
pwd=config.get('DatabaseSection', 'database.password')
dbname=config.get('DatabaseSection', 'database.dbname')

print("Hostname:",host)
print("User:",user)
print("Password:",pwd)
print("dbname:",dbname)


db = MySQLdb.connect(host,    # your host, usually localhost
                     user,         # your username
                     pwd,  # your password
                     dbname)        # name of the data base
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM contDef")

def fetchData():
    jFileName="demodb.json"
    df = pd.DataFrame()
    df = cur.fetchall();
    df.to_json(jFileName)
    return jFileName
# print all the first cell of all the rows
    
def list():
    for row in cur.fetchall():
        print (row[0] , row[1] , row[2])

db.close()


if __name__ == '__main__':
    df = fetchData()