from wtforms.fields import BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf import FlaskForm
from datetime import datetime


class LoginForm(FlaskForm):
  employee_number = StringField('Employee number', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Login')
