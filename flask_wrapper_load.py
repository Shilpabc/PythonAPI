# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:00:04 2019

@author: Shilpa_Chikkannavar
"""

from flask import Flask, render_template, request, jsonify
from getJsonData import readJsonData
from createJsonFromDB import getJsonFname

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify("PAGE NOT FOUND")

@app.route('/loadlist', methods=['GET'])
def getprod():

    try:  
        jsonFname = getJsonFname()
        res = readJsonData('M2.json')

    except Exception as e:
	    return(str(e) + "ERROR")
        
        
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)




    