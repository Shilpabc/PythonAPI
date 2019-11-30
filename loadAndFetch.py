# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:02:54 2019

@author: Shilpa_Chikkannavar
"""

from getdata import fetchData

def fetchProd(prod):
    
    print("In fetchProd: ",prod)
    contList = fetchData()
    print("Data fetched")
    print(contList)
    
    
    for p in contList:
        if (p[0] == prod):
            print("Matched")
            print(p[0])
            result = p
            break
        else:
            result = "NOT FOUND"
            continue
        
    return result

if __name__ == '__main__':
    print (fetchProd("gitlab"))
    
