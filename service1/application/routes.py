from flask import render_template, request

from application import app, db

from application.models import Affirmations

from application.forms import 


@app.route('/')
@app.route('/home', methods='GET','POST')

def home():
    
    getfortune = requests.get('http://service4:5000/fortune')

    return render_template('home.html', title='Home', Fortune=getfortune)


#@app.route('/home/fortune', methods=['GET','POST'])

#def fortune():

 ##   fortune = requests.post('http://service4:5000/fortune')
