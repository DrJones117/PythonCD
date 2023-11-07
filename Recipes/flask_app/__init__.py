from flask import Flask, session

DATABASE = "recipes_db"

app = Flask(__name__)
app.secret_key = "nuthaKey"