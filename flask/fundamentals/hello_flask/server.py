from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/user/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username" + username + ", id" + id

@app.route('/hello2/<name>/<int:num>')
def hello2(name, num):
    return f"Hello, {name * num}"

if __name__=="__main__":
    app.run(debug=True)

