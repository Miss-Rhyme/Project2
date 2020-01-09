from flask import render_template,request

from application import app, db

from application.models import Fortune

import requests

@app.route('/getdcode', methods=['GET', 'POST'])

def getcode():

    getletter = requests.post( "http://service2:5000/codeLetter" )
    

    getnumber = requests.post( "http://service3:5000/codeNumeber" )


    fortunecode = str(getletter) + str(getnumber)

    fortunedraw = Fortune.query.filter_by(code = fortunecode).all()

    return {'fortune':fortunedraw}
