from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User


@app.route('/')
def main():
    return redirect('/main')

# Main Form page
@app.route('/main')
def users():
    return render_template('main_page.html', users=User.get_everything())

# Edit Form page
@app.route('/main/edit/<int:id>')
def edit(id):
    return render_template("edit_user.html", user = User.get_single(id))

# Show User
@app.route('/main/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template('show_user.html', user=User.get_single(id))

# Update User
@app.route('/main/update/<int:id>', methods=['POST'])
def update(id):
    data = {
        "id": id,
        **request.form
    }
    User.update(data)
    return redirect(f'/main/show/{id}')

# Delete User
@app.route('/main/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/main')

# Create User page
@app.route('/main/new')
def user():
    return render_template("make_user.html")


# Saves new users info
@app.route('/main/create', methods=['POST'])
def new():
    user_id = User.save_user(request.form)
    return redirect(f'/main/show/{user_id}')


