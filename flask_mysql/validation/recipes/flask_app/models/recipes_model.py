from flask_app.models.login_model import User
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash


class Recipe:
    def __init__( self , data ):
        self.id_recipes = data['id_recipes']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_30_min = data ['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create_recipe(cls, data):
        query = 'INSERT INTO recipes (name, description, instructions, date, under_30_min, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(under_30_min)s, NOW(), NOW(), %(user_id)s )'
        connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def get_recipe(cls):
        query = 'SELECT * FROM recipes'
        results = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        print(recipes)
        return recipes

    @classmethod
    def get_recipes_by_id(cls, data):
        query = 'SELECT * FROM recipes WHERE id_recipes = %(id_recipes)s'
        results = connectToMySQL('recipes_schema').query_db(query, data)
        recipe = Recipe(results[0])
        return recipe
    
    @classmethod
    def update_recipe(cls, data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s WHERE id_recipes = %(id_recipes)s'
        connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = 'DELETE FROM recipes WHERE id_recipes = %(id_recipes)s'
        connectToMySQL('recipes_schema').query_db(query, data)


    @staticmethod
    def validate_recipe(data):
        is_valid = True
        query = 'SELECT * FROM recipes'
        connectToMySQL('recipes_schema').query_db(query, data)

        if len(data['name']) <3 or len(data['name']) > 45:
            is_valid = False
            flash('Recipe name should be between 3 and 45 characters long')
        
        if len(data['description']) <3 or len(data['description']) > 255:
            is_valid = False
            flash('Recipe description should be between 3 and 45 characters long')

        if len(data['instructions']) <3 or len(data['instructions']) > 255:
            is_valid = False
            flash('Recipe instructions should be between 3 and 45 characters long')
        if len(data['date']) != 10:
            is_valid = False
            flash('Date not correct format.')
        
        # if len(data['under_30_min']) = 0 or len(data['under_30_min']) =1:
        #     is_valid = False
        #     flash('Please select')

        return is_valid
        