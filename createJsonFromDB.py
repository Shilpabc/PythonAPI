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

jsonPath=config.get('CacheDB', 'cache.folder')
jFileName=config.get('CacheDB', 'jsonfilename')
fName = jsonPath + "\\" + jFileName

def fetchData():
    
    db = MySQLdb.connect(host,user,pwd,dbname) 
    cur = db.cursor()
    cur.execute("SELECT * FROM contDef")
    tp=pd.DataFrame(list(cur.fetchall()),columns=['name','repo','image','essential'])
    df = pd.DataFrame(tp)
    df.to_json(fName,orient ='index')
    db.close()
    return df

if __name__ == '__main__':
    df = fetchData()

    

    