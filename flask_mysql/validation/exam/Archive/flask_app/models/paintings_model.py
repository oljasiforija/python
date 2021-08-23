from flask_app.models.login_model import User
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

class Painting():
    def __init__(self, data):
        self.id_painting = data['id_painting']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data ['user_id']

    @classmethod
    def create_painting(cls, data):
        query = 'INSERT INTO paintings(title, description, price, created_at, updated_at, user_id) VALUES (%(title)s, %(description)s, %(price)s, NOW(), NOW(), %(user_id)s)'
        connectToMySQL('exam_schema').query_db(query, data)

    @classmethod
    def get_paintings(cls):
        query = 'SELECT * FROM paintings'
        results = connectToMySQL('exam_schema').query_db(query)
        paintings = []
        for painting in results:
            paintings.append(cls(painting))
        print(paintings)
        return paintings
        
    @classmethod
    def get_painting_by_id(cls, data):
        query = 'SELECT * FROM paintings WHERE id_painting = %(id_painting)s'
        results = connectToMySQL('exam_schema').query_db(query, data)
        painting = Painting(results[0])
        return painting

    @classmethod
    def update_painting(cls,data):
        query = 'UPDATE paintings SET title = %(title)s, description = %(description)s, price = %(price)s WHERE id_painting = %(id_painting)s'
        results = connectToMySQL('exam_schema').query_db(query, data)
        return results

    @classmethod
    def delete_painting(cls, data):
        query = 'DELETE FROM paintings WHERE id_painting = %(id_painting)s'
        results = connectToMySQL('exam_schema').query_db(query, data)
        return results

    @staticmethod
    def validate_painting(data):
        is_valid = True
        query = 'SELECT * FROM paintings'
        connectToMySQL('exam_schema').query_db(query, data)

        if len(data['title']) < 2 or len(data['title']) > 50:
            is_valid = False
            flash('Painting title should be between 2 and 50 characters long.')
        if len(data['description']) <10 or len(data['description']) > 255:
            is_valid = False
            flash('Painting description should be between 10 and 255 characters long.')
        if int(data['price']) == 0:
            is_valid = False
            flash('Price needs to be greater than $0')
        return is_valid
