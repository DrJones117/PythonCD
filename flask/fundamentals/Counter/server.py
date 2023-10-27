from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '15784'

@app.route('/')
def counter():
    session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    session['count'] = 0
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)