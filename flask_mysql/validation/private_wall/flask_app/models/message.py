from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.information = data['information']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
