from wtforms import form, StringField, SelectField, TextField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class StudentNameCity(FlaskForm):
    studentName = SelectField('Student Name')
    submit = SubmitField('Go')
