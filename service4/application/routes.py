from flask import render_template,request

from application import app, db

from application.models import Fortune

import requests

@app.route('/getcode', methods=['GET', 'POST'])

def getcode():

    getletter = requests.get( "http://service2:5000/codeLetter" )
    

    getnumber = requests.get( "http://service3:5000/codeNumber" )


    codels = []

    codels.append(getnumber)
    codels.append(getletter)

    coderesult = "".join(codels)


    fortuneresult = Fortune.query.filter_by(fortune = coderesult).first()

    return {'fortune':fortuneresult}
