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

# Grabs Dojo and redirects to Show Dojo Page
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
