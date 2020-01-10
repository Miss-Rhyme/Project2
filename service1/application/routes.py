from flask import render_template, request

from application import app, db

from application.models import Fortune

from application.forms import FortuneButton

import requests


@app.route('/')
@app.route('/home', methods=['GET','POST'])

def home():

    form = FortuneButton()

    if request.method=='POST':
        
      ##  getfortune = requests.get('http://service4:5004').text
        fortune=requests.post('http://service4:5004').text

         return render_template('home.html', title='Home', fortune=fortune, form=form)
    else:
        return render_template('home1.html', title='Home', form=form)

