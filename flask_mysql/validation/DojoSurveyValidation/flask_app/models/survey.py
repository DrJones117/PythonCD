from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name should be greater than two characters.")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Please choose a location.")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Choose your favorite language.")
        if len(survey['comment']) < 10:
            is_valid = False
            flash("Leave a comment please")
        return is_valid



    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos (name, location, language, comment, created_at, updated_at) 
        VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());
        """

        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return results



    @classmethod
    def get_latest_survey(cls):
        query = """
        SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;
        """
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        if results:
            return Survey(results[0])
        else:
            return None

