from flask import render_template,request

from application import app

import random

@app.route('/codenumber', methods=['POST'])

def codenumber():
    
    num = random.randint(1,5)

    return {'numbervalue':f'{num}'}
