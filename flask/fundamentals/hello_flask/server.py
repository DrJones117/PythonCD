from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/hello_person/<string:name>')
def hello_person(name):
    return 'Hello ' + name

@app.route('/hello_num/<string:input>/<int:num>')
def hello_num(input, num):
    return f"{input * num}"
if __name__=="__main__":
    app.run(debug=True)

