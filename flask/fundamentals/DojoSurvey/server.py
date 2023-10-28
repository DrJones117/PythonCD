from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'something'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/render_result', methods=['POST'])
def render():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
