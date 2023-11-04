from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.email import Email


@app.route('/')
def main():
    return redirect('/log_in')

@app.route('/log_in')
def render_log_in():
    print('rendering log_in page')
    return render_template('index.html')

@app.route('/log_in/submit', methods=['POST'])
def submit():
    print(request.form)
    if not Email.validator(request.form):
        print("oops. something went wrong.")
        return redirect('/')
    print('getting results...')
    Email.save(request.form)
    return redirect('/log_in/result')

@app.route('/log_in/result')
def display():
    print('rendering results page.')
    emails = Email.get_all()
    print(emails)
    return render_template('result.html', emails = emails)