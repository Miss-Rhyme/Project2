from flask import request, jsonify
from application import app, db

from application.models import Fortune

import requests

@app.route('/', methods=['GET', 'POST'])

def getcode():

    getletter=requests.get( 'http://service2:5002').text
    

    getnumber=requests.get( 'http://service3:5003').text


    codels = []

    codels.append(getletter)
    codels.append(getnumber)


    coderesult = "-".join(codels)

    fortuneresult = Fortune.query.filter_by(code=coderesult).first()

    fortune = fortuneresult.fortune

    code = fortuneresult.code


    cookie =  {'fortune' : fortune, 'code' : code}

    return jsonify(cookie)
