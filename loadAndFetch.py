# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:02:54 2019

@author: Shilpa_Chikkannavar
"""

from getJsonData import readJsonData

def fetchProd(prod):
    
    print("In fetchProd: ",prod)
    contList = readJsonData('M2.json')
    print("Data fetched")
    print(contList)
    
    
    for p in contList:
        if (p['name'] == prod):
            print("Matched")
            print(p['name'])
            result = p
            break
        else:
            result = "NOT FOUND"
            continue
        
    return result

if __name__ == '__main__':
    print (fetchProd("gitlab"))
    
