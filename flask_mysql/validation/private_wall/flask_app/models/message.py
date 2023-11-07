from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE
from flask_app.models.user import User

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.information = data['information']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_to_id = data['user_to_id']
        self.user_from_id = data['user_from_id']

# Sends the message to the database
    @classmethod
    def send_message(cls, form):
        query = """
        INSERT INTO messages (information, created_at, updated_at, user_to_id, user_from_id)
        VALUES (%(information)s, NOW(), NOW(), %(user_to_id)s, %(user_from_id)s)
        """
        return connectToMySQL(DATABASE).query_db(query, form)

# Displays the users messages
    @classmethod
    def display_messages(cls):
        query = """
        SELECT * FROM messages 
        """
        results = connectToMySQL(DATABASE).query_db(query)
        messages = []
        if results:
            for row in results:
                messages.append(cls(row))
            return messages
        return messages

# Deletes a message
    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM messages WHERE id = %(id)s
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

