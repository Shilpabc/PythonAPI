# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:02:54 2019

@author: Shilpa_Chikkannavar
"""
import configparser
import pandas as pd
from getJsonData import readJsonData

config = configparser.RawConfigParser()
config.read('ConfigFile.properties')

jsonPath=config.get('CacheDB', 'cache.folder')
jFileName=config.get('CacheDB', 'jsonfilename')
fName = jsonPath + "\\" + jFileName


def fetchProd(prod):
    
    print("In fetchProd: ",prod)
    print("Json FileName: ",fName)

    contList = pd.DataFrame()
    contList = readJsonData(fName)
    print(contList)
    for p in contList['name']:
        print(p)
        if (p == prod):
            print("Matched")
            result = contList.loc[contList['name'] == p ]
            break
        else:
            result = "NOT FOUND"
            continue
        
    return result

if __name__ == '__main__':
    df = fetchProd("gitlab")
    print(df)
    
