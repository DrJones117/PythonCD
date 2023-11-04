from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/render/survey', methods=['POST'])
def render_survey():
    print(request.form)
    if Survey.is_valid(request.form):
        print("Getting results...")
        Survey.save(request.form)
        return redirect('/result')
    else:
        return redirect('/')

@app.route('/result')
def result():
    return render_template('result.html', survey = Survey.get_latest_survey())
