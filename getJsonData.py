# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:22:16 2019

@author: Shilpa_Chikkannavar
"""
import json
import configparser
import pandas as pd
config = configparser.RawConfigParser()
config.read('ConfigFile.properties')

jsonPath=config.get('CacheDB', 'cache.folder')
jFileName=config.get('CacheDB', 'jsonfilename')
fName = jsonPath + "\\" + jFileName


def readJsonData(fName):
    print("In readJsonData")
    print("Json File Name",fName)
    #with open(fName) as json_file:
    data = pd.read_json(fName,orient='index')
    #read_json(json_file)
    return data



if __name__ == '__main__':
    df = readJsonData(fName)
    print (df)