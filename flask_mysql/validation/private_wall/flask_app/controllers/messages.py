from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message


# Renders the Login page
@app.route('/')
def index():
    return render_template('login.html')

# Calls the Login function
@app.route('/login', methods = ['POST'])
def login():
    logged_user = User.login(request.form)
    if logged_user:
        session['id'] = logged_user.id
        return redirect('/home_page')
    else:
        return redirect('/')

# Logs the user out
@app.route('/home_page/logout')
def logout():
    session.clear()
    return redirect('/')

# Calls the register function and adds the new user to the database
@app.route('/add_user', methods = ['POST'])
def add_user():
    if User.validator(request.form):
        print("working")
        session['id'] = User.register(request.form)
        return redirect('/home_page')
    else:
        return redirect('/')

# Renders the home page if the user's id is in session
@app.route('/home_page')
def home_page():
    if not 'id' in session:
        return redirect('/')
    user = User.get_one(session['id'])
    return render_template("home.html", user = user)