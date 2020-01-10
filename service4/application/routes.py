from flask import render_template,request

from application import app, db

from application.models import Fortune

import requests

@app.route('/fortune', methods=['GET', 'POST'])

def getcode():

    getletter = requests.POST.get( "http://service2:5002/codeLetter" )
    

    getnumber = requests.POST.get( "http://service3:5003/codeNumber" )


    codels = []

    codels.append(getnumber)
    codels.append(getletter)

    coderesult = "".join(codels)


    fortuneresult = Fortune.query.filter_by(fortune = coderesult).first()

    #return {'fortune':fortuneresult}

    return fortuneresult
