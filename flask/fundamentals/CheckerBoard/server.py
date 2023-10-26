from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<int:num>/<int:num2>')
def standard(num, num2):
    return render_template('index.html', num=num, num2=num2)

if __name__=="__main__":
    app.run(debug=True)