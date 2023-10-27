from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def open():
    return ("Hello!")
    
@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/hello_person/<string:name>')
def hello_person(name):
    return 'Hello ' + name

@app.route('/hello_num/<string:input>/<int:num>')
def hello_num(input, num):
    return f"{input * num}"

@app.route('/lists')
def render_lists():
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5],  students = student_info)

if __name__=="__main__":
    app.run(debug=True)
