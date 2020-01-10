from flask import render_template,request

from random import randint

from application import app

import requests


@app.route('/', methods=['GET', 'POST'])

def codenumber():
    
    num = random.randint(1)

    #return {'numbervalue':f'num}'}

    return str(num)


