from flask import render_template,request

from application import app

import requests

import random

@app.route('/codeletter', methods=['POST'])

def codeletter():

    letters = ['A', 'B', 'C', 'D']

    letter = random.choice(letters)

    #return {'lettervalue':f'{letter}'}

    return letter
