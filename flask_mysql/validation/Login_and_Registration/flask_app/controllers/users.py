from flask_app import app
from flask_app.models.user import User
from flask import render_template, request, redirect, session



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods = ['POST'])
def login():
    logged_user = User.login(request.form)
    if logged_user:
        return redirect('/home_page')
    else:
        return redirect('/')

@app.route('/add_user', methods = ['POST'])
def add_user():
    User.register(request.form)
    return redirect('/home_page')

@app.route('/home_page')
def home_page():
    return render_template("home.html")