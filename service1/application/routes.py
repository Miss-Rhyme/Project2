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

        getfortune = requests.get('http://service4:5004/fortune')

        return render_template('home.html', title='Home', Fortune=getfortune, form=form)

    return render_template('home1.html', title='Home', form=form)

