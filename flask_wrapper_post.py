# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:00:04 2019

@author: Shilpa_Chikkannavar
"""

from flask import Flask, render_template, request, jsonify
from updateRecords import updateRec

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify("PAGE NOT FOUND")

@app.route('/addProd', methods=['GET'])
def getprod():
   
    prod = None
    repo = None
    image = None
    essential = None
    try:  
        if 'prod' in request.args:
            prod = request.args['prod']
            print(prod)
        if 'repo' in request.args:
            repo = request.args['repo']
            print(repo)
        if 'image' in request.args:
            image = request.args['image']
            print(image)
        if 'essential' in request.args:
            essential = request.args['essential']
            print(essential)
    except Exception as e:
        return(str(e) + "ERROR")
    
    if (prod) and (repo) and (image) and (essential):
        rList = [prod,repo,image,essential]
        updateRec(rList)
        rList = "Record Inserted"
    else:
        rList = "Require complete list of param: Prod, Repo,Image,Essential(True/False)"
    print(rList)
    return jsonify(rList)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)




    