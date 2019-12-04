# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:00:04 2019

@author: Shilpa_Chikkannavar
"""

from flask import Flask, render_template, request, jsonify
from getJsonData import readJsonData
import pandas as pd

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify("PAGE NOT FOUND")

@app.route('/loadlist', methods=['GET'])
def getprod():

    try:  
        df = pd.DataFrame()
        df = readJsonData()
        res = df.to_json(orient='index')
    except Exception as e:
	    return(str(e) + "ERROR")
        
        
    return res

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
