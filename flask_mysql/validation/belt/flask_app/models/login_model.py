from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")



class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data ['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cars = []

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() )"
        connectToMySQL('belt_schema').query_db(query, data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('belt_schema').query_db(query, data)
        return cls(results[0])
    
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL('belt_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @staticmethod
    def validate_user(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('belt_schema').query_db(query,data)

        if len(data['first_name']) < 2 or len(data['first_name']) > 50:
            is_valid = False
            flash ('First name should be between 2 or 50 characters.')
        

        if len(data['last_name']) < 2 or len(data['last_name']) > 50:
            is_valid = False
            flash ('Last name should be between 2 or 50 characters.')

        if len(data['email']) > 255:
            is_valid = False
            flash('Email is too long.')

        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Email is not formatted correctly.')

        if len(data['password']) < 8:
            is_valid = False
            flash ('Password should be at least 8 characters long.')
        if not PASSWORD_REGEX.match(data['password']):
            is_valid = False
            flash('Password must be at least 8 characters long, have at least (1) upper-case letter, have at least (1) lower-case letter and at least (1) number.')

        if not data['password'] == data ['confirm_password']:
            is_valid = False
            flash('Password and confirm password do not match.')
        if len(results) >=1:
            is_valid = False
            flash('User in use')

        return is_valid