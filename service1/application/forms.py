from flask_wtf import FlaskForm
from application import db
from wtforms import SubmitField

from application.models import Lucky, Unlucky

class FortuneDraw(FlaskForm):
    
    submit = SubmitField('Eat a cookie and get a fortune!')
