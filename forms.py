from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class WorkoutForm(FlaskForm):
    goal = StringField("What is your training goal?", validators=[InputRequired()])
    days_per_week = StringField("How many days per week can you workout", validators=[InputRequired()])
    time_avaliable = StringField("How many minutes will you spend each workout", validators=[InputRequired()])
    equipment = StringField("What equipment/gym availability do you have", validators=[InputRequired()])
