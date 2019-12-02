# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:22:16 2019

@author: Shilpa_Chikkannavar
"""
import json
import pandas as pd

def readJsonData(jsonFileName):
    with open(jsonFileName) as json_file:
        data = json.load(json_file)
        
    contDict = data['containerDefinitions']
    return contDict



if __name__ == '__main__':
    df = readJsonData('M2.json')
    print (df)