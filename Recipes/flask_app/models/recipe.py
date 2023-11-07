from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, DATABASE
from flask import flash
from flask_app.models.user import User


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.under_30_minutes = data['under_30_minutes']
        self.cooked_made = data['cooked_made']
        self.user_id = data['user_id']

    # Posts a recipe to the logged in user
    @classmethod
    def add_recipe(cls, form):
        query = """
        INSERT INTO recipes (name, description, instructions, under_30_minutes, cooked_made, user_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30_minutes)s, %(cooked_made)s, %(user_id)s);
        """
        return connectToMySQL("recipes_db").query_db(query, form)

    @classmethod
    def delete_recipe(cls, form):
        query = """
        INSERT INTO recipes (name, description, instructions, under_30_minutes, cooked_made, user_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30_minutes)s, %(cooked_made)s, %(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, form)

    # Displays all the recipes
    @classmethod
    def display_recipes(cls):
        query = """
        SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;
        """
        results = connectToMySQL('recipes_db').query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            # For each row pull out and instantiate each recipe. Get data from user and turn it into an object. accociate them with each other.
            user_data = {
                'id': row['id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            recipe.user = User(user_data)
            recipes.append(recipe)
        return recipes

    # Gets one recipe by it's id with the data of the creator
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM recipes
        JOIN users ON recipes.user_id = users.id
        WHERE recipes.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        recipe_data = results[0]
        recipe = cls(recipe_data)
            
        user_data = {
            'id': recipe_data['id'],
            'first_name': recipe_data['first_name'],
            'last_name': recipe_data['last_name'],
            'email': recipe_data['email'],
            'password': recipe_data['password'],
            'created_at': recipe_data['created_at'],
            'updated_at': recipe_data['updated_at']
        }
        recipe.user = User(user_data)
        return recipe


# Updates a recipe using a given id
    @classmethod
    def update(cls, data):
        query = """
        UPDATE recipes SET 
        name = %(name)s,
        description = %(description)s,
        instructions = %(instructions)s,
        updated_at = NOW()
        WHERE id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

# Deletes a recipe
    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM recipes WHERE id = %(id)s
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @classmethod
    def validate_recipe(cls, form):
        is_valid = True
        if len(form['name']) < 2:
            flash("Please provide a name.", "add_err")
            is_valid = False
        if len(form['description']) < 10:
            flash("Please provide a detailed description", "add_err")
            is_valid = False
        if len(form['instructions']) < 40:
            flash("Please provide detailed instructions", "add_err")
            is_valid = False
        if len(form['cooked_made']) == 0:
            flash("Please provide a date.", "add_err")
            is_valid = False
        return is_valid

