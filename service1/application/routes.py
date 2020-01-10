from flask import render_template, request

from application import app, db

from application.models import Fortune

from application.forms import FortuneButton

import requests


@app.route('/')
@app.route('/home', methods=['GET','POST'])

def home():

   # form = FortuneButton()

    #if form.is_submitted():
        
    fortune = requests.get('http://service4:5004')
        ## fortune=requests.post('http://service4:5004').text
        
    app.logger.info("FORTUNE PLS")
        
     #   return fortune

    return render_template('home.html', title='Home', fortune=fortune.json()) #, form=form)

   # return render_template('home1.html', title='Home', form=form)

