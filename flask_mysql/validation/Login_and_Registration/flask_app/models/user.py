from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

from flask_bcrypt import Bcrypt  
bcrypt = Bcrypt(app)


class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.name = data['name']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def register(cls, form):
        hash = bcrypt.generate_password_hash(form["password"])
        data = {
            **form,
            "password": hash
        }
        query = """
        INSERT INTO users (email, name, password)
        VALUES (%(email)s, %(name)s, %(password)s);
        """
        return connectToMySQL("accounts_db").query_db(query, data)


    @classmethod
    def find_user(cls, email):
        data = {
            "email": email
        }
        query = """
        SELECT * FROM users WHERE email = %(email)s;
        """
        results = connectToMySQL("accounts_db").query_db(query, data)
        if results:
            return cls(results[0])
        else:
            return False


    @classmethod
    def login(cls, form):
        user = cls.find_user(form['email'])
        if user:
            if bcrypt.check_password_hash(user.password, form['password']):
                return user
            else:
                flash("Bad Login", "login_err")
                return False
        else:
            flash("Bad Login", "login_err")
            return False
