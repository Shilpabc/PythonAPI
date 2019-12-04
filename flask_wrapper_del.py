# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:00:04 2019

@author: Shilpa_Chikkannavar
"""

from flask import Flask, render_template, request, jsonify
import pandas as pd
from loadAndFetch import fetchProd 
#from createJsonFromDB import getJsonFname


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify("PAGE NOT FOUND")

@app.route('/getprod', methods=['GET'])
def getprod():
    
    df = pd.DataFrame()
    try:  
        if 'prod' in request.args:
            prod = request.args['prod']
            df = fetchProd(prod)
            print("Result",df)
            res = df.to_json()
        else:
            res = jsonify("Please padd a Prod to be queried")

    except Exception as e:
	    return(str(e))
        
        
    return res

if __name__ == '__main__':
    app.run(host='localhost', port=5000)




    