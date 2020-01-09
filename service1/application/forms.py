from flask_wtf import FlaskForm
from application import db
from wtforms import SubmitField

from application.models import Fortune

class FortuneButton(FlaskForm):
    
    submit = SubmitField('Tell me my fortune!')
