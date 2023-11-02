from flask import Flask, render_template, request, redirect

from main import User

app=Flask(__name__)

@app.route('/')
def main():
    return redirect('/main')

@app.route('/main')
def users():
    return render_template('main_page.html', users=User.get_everything())

@app.route('/main/new')
def user():
    return render_template("make_user.html")

@app.route('/main/create', methods=['POST'])
def new():
    print(request.form)
    User.save_user(request.form)
    return redirect('/main')

if __name__ == "__main__":
    app.run(debug = True)