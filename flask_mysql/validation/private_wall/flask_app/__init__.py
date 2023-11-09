from flask import Flask, session

DATABASE = "python_exam_db"

app = Flask(__name__)
app.secret_key = "secretkey"