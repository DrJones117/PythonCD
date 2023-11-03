from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def dojo():
    return redirect('/dojo')


# Main Page
@app.route('/dojo')
def dojo_render():
    return render_template('dojo.html', dojos= Dojo.get_all())

# Grabs ID and redirects to Show Dojo Page
@app.route('/dojo/grab/<int:id>')
def grab_id(id):
    print('grabbing id')
    data = {
        "id": id
    }
    Dojo.get_one(data)
    return redirect(f'/dojo/show/{id}')

# Show Dojo Page
@app.route('/dojo/show/<int:id>')
def dojo_show(id):
    print("accessing show route")
    data = {
        "id": id
    }
    dojo = Dojo.get_one(id)
    ninjas = Ninja.get_ninjas(id)
    return render_template('dojo_show.html', dojo = dojo, ninjas = ninjas)

@app.route('/dojo/create', methods = ['POST'])
def create_dojo():
    print(request.form)
    dojos = Dojo.create_dojo(request.form)
    return redirect('/')

# Create Ninja Route
@app.route('/ninja/create', methods = ['POST'])
def create_ninja():
    print(request.form)
    ninjas = Ninja.create_ninja(request.form)
    return redirect(f'/dojo/show/{request.form["dojo_id"]}')

# Add Ninja Page
@app.route('/dojo/add_ninja')
def render_add():
    print('direct to add page')
    return render_template('ninja.html', dojos = Dojo.get_all())
