from flask import Flask, render_template, redirect, session, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sushiKey import API_SECRET_KEY
from workout_regex import extract_json_object

from models import db, connect_db, User, Routine
from forms import UserForm, WorkoutForm
from bardapi import Bard


bard = Bard(token=API_SECRET_KEY)

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///workout_routine_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "WorkSushiOutRoutine"

def return_question(goal, days, time, equipment):
    return f"Give me a workout plan in the form of a json object that will make me {goal}. I can work out {days} days a week and {time} minutes each workout. I have {equipment}. The format of the json object is days, exercises, sets, and reps. Days will be an arrays of days that will be working out. Exercises will be an array of arrays that is the same length at the days and represent the exercises done each day. Sets and reps correlate to each of the exercises and should be formatted the same way as the exercises. Days, exercises, sets and reps should all be their own key and should be the same size as the exercises key. Thank you."

def parse_response(text):
    pass

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=["GET", "POST"])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.register(username, password)
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        return redirect('/form')

    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome Back, {user.username}", "success")
            session['user_id'] = user.id
            return redirect('/form')
        else:
            form.username.errors = ['Invalid username/password']

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_user():
    session.pop('user_id')
    flash("Goodbye")
    return redirect('/')

@app.route('/form', methods=['GET', 'POST'])
def survey():
    form = WorkoutForm()
    if form.validate_on_submit():
        goal = form.goal.data
        days_per_week = form.days_per_week.data
        time_avaliable = form.time_avaliable.data
        equipment = form.equipment.data
        answer = bard.get_answer(return_question(goal, days_per_week, time_avaliable, equipment))["content"]
        workout = extract_json_object(answer)
        return render_template('results.html', days=workout["days"], exercises=workout["exercises"], sets=workout["sets"], reps=workout["reps"])
    return render_template("survey.html", form=form, script_src="script.js")