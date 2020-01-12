from flask import render_template,request

import random

from application import app

import requests


@app.route('/', methods=['GET', 'POST'])

def codenumber():
    
    num = random.randint(1,4)


    return str(num)


