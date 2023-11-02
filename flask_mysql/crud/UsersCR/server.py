from flask import Flask, render_template, request, redirect

from main import User

app=Flask(__name__)

@app.route('/')
def main():
    return redirect('/main')

# Edit Form page
@app.route('/edit/<int:id>')
def edit(id):
    return render_template("edit_user.html", user = User.get_single(id))

# Update User
@app.route('/main/update')
def update():
    User.update(request.form)
    return redirect('/main')

# Main Form page
@app.route('/main')
def users():
    return render_template('main_page.html', users=User.get_everything())

# Create User page
@app.route('/main/new')
def user():
    return render_template("make_user.html")

# Saves new users info
@app.route('/main/create', methods=['POST'])
def new():
    User.save_user(request.form)
    return redirect('/main')


if __name__ == "__main__":
    app.run(debug = True)