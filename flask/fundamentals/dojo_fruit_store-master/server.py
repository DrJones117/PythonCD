from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    print(int(request.form["strawberry"]) + int(request.form["raspberry"]) + int(request.form["apple"]))
    return render_template("checkout.html", first=request.form["first_name"], last=request.form["last_name"], 
    id=request.form["student_id"], one=request.form["strawberry"], two=request.form["raspberry"], three=request.form["apple"])

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)