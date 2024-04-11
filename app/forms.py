# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class MovieForm(FlaskForm):
    title =StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])
    
    
