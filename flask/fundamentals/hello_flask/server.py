from flask import Flask, render_template

app = Flask(__name__)
@app.route('/color/play/<int:num>')
def play(color, num):
    return render_template('index.html',color=color, num=num)

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
