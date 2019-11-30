# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:00:04 2019

@author: Shilpa_Chikkannavar
"""

from flask import Flask, render_template, request, jsonify
from loadAndFetch import fetchProd 


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify("PAGE NOT FOUND")

@app.route('/getprod', methods=['GET'])
def getprod():

    try:  
        if 'prod' in request.args:
            prod = request.args['prod']
            res = fetchProd(prod)
        else:
            res = "PARAM REQUIRED"

    except Exception as e:
	    return(str(e))
        
        
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)




    