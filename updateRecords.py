# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:07:29 2019

@author: Shilpa_Chikkannavar
"""
import MySQLdb
import json
import pandas as pd
import configparser
from createJsonFromDB import fetchData

def updateRec (rList,op):
    config = configparser.RawConfigParser()
    config.read('ConfigFile.properties')
    
    host=config.get('DatabaseSection', 'database.service')
    user=config.get('DatabaseSection', 'database.user')
    pwd=config.get('DatabaseSection', 'database.password')
    dbname=config.get('DatabaseSection', 'database.dbname')
    
    db = MySQLdb.connect(host,    # your host, usually localhost
                         user,         # your username
                         pwd,  # your password
                         dbname)        # name of the data base
    cur = db.cursor()
    if rList[3] is True:
        ess = str(1)
    else:
        ess = str(0)
    if op is 'insert':
        query = "INSERT INTO contDef VALUES ('" + rList[0] +"','" + rList[1] + "','" + rList[2] + "'," + ess + ");"
    elif op is 'delete':
        query = "DELETE FROM contDef WHERE" + "name=" + prod

        
    print (query)
    # Use all the SQL you like
    cur.execute(query)
    db.commit()

    db.close()
    fetchData()
    

if __name__ == '__main__':
    rList = ['git123','REPO','IMAGE','True']
    df = updateRec(rList)
    print (df)
    
    