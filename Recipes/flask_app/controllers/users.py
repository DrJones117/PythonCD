from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


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
    recipes = Recipe.display_recipes()
    return render_template("home.html", user = user, recipes = recipes)


# ====== Recipe Routes ======

# Add recipe route
@app.route('/recipe')
def recipe():
    if not 'id' in session:
        return redirect('/')
    user = User.get_one(session['id'])
    return render_template("add_recipe.html", user = user)


# Calls the add_recipe function and redirects to the home_page
@app.route('/recipe/add', methods = ['POST'])
def add_recipe():
    if Recipe.validate_recipe(request.form):
        print("adding recipe")
        recipe = Recipe.add_recipe(request.form)
        return redirect("/home_page")
    else:
        return redirect('/recipe')

# Renders the edit page
@app.route('/recipes/<int:id>/edit')
def render_edit(id):
    data = {
        "id": id
    }
    user = User.get_one(session['id'])
    recipe = Recipe.get_one(data)
    return render_template('edit_recipe.html', recipe = recipe, user = user)

# Calls the update function
@app.route('/recipes/<int:id>/update', methods=['POST'])
def update(id):
    if Recipe.validate_recipe(request.form):
        data = {
            "id": id,
            **request.form
        }
        Recipe.update(data)
        return redirect('/home_page')
    else:
        return redirect(f'/recipes/{id}/edit')

# Calls the delete function
@app.route('/recipes/<int:id>/delete')
def delete(id):
    data = {
        "id": id
    }
    Recipe.delete(data)
    print('deleted')
    return redirect('/home_page')

# Redirects to the show recipe page
@app.route('/recipes/<int:id>/show')
def show_recipe(id):
    data = {
        "id": id
    }
    user = User.get_one(session['id'])
    recipe = Recipe.get_one(data)
    return render_template('show_recipe.html', recipe = recipe, user = user)


