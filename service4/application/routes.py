from flask import request

from application import app, db

from application.models import Fortune

import requests

@app.route('/', methods=['GET', 'POST'])

def getcode():

    getletter=requests.get( 'http://service2:5002').text
    

    getnumber=requests.get( 'http://service3:5003').text


    codels = []

    codels.append(getnumber)
    codels.append(getletter)

    coderesult = "-".join(codels)


#    fortuneresult = Fortune.query.filter_by(code=coderesult).first()

    #return {'fortune':fortuneresult}

#    return fortuneresult

    return coderesult
