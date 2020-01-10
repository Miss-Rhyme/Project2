from flask import render_template,request

import random

from application import app

import requests


@app.route('/', methods=['GET', 'POST'])

def codenumber():
    
    num = random.randint(1,2)

    #return {'numbervalue':f'num}'}

    return str(num)


