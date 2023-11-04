from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Email:

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validator(email):
        is_valid = True
        query = """
        SELECT * FROM emails WHERE email = %(email)s;
        """
        results = connectToMySQL("emails_db").query_db(query, email)
        if results and len(results) >= 1:
            flash("Email already taken.")
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("invalid email bruh")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO emails (email, created_at, updated_at)
        VALUES (%(email)s, NOW(), NOW())
        """
        results = connectToMySQL("emails_db").query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM emails;
        """
        results = connectToMySQL("emails_db").query_db(query)
        emails = []
        for result in results:
            emails.append( cls(result))
        return emails
