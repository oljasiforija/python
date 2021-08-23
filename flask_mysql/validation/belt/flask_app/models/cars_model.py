from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_app.models.login_model import User


class Car():
    def __init__(self, data):
        self.id = data['id']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
    
    @classmethod
    def new_car(cls, data):
        query = 'INSERT INTO cars (price, model, make, year, description, created_at, updated_at, user_id) VALUES (%(price)s, %(model)s, %(make)s, %(year)s, %(description)s, NOW(), NOW(), %(user_id)s)'
        connectToMySQL('belt_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM cars'
        results = connectToMySQL('belt_schema').query_db(query)
        cars = []
        for car in results:
            cars.append(cls(car))
        print(cars)
        return cars

    @classmethod
    def cars_n_users(cls):
        query = 'SELECT * FROM cars JOIN users ON cars.user_id = users.id'
        results = connectToMySQL('belt_schema').query_db(query)

        cars = []

        for row in results:
            car = Car(row)
            user_data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row ['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            user = User(user_data)
            car.user = user
            cars.append(car)
        return cars

    @classmethod
    def cars_n_users_by_id(cls, data):
        query = 'SELECT * FROM cars JOIN users ON cars.user_id = users.id WHERE cars.id = %(id)s'
        results = connectToMySQL('belt_schema').query_db(query, data)[0]
        car = Car(results)
        user_data = {
            'id' : results['users.id'],
            'first_name' : results['first_name'],
            'last_name' : results['last_name'],
            'email' : results['email'],
            'password' : results ['password'],
            'created_at' : results['users.created_at'],
            'updated_at' : results['users.updated_at']
        }
        car.user = User(user_data)
        return car

    
    @classmethod
    def get_car_by_id(cls,data):
        query = 'SELECT * FROM cars WHERE id = %(id)s'
        results = connectToMySQL('belt_schema').query_db(query, data)
        car = Car(results[0])
        return car

        
    @classmethod
    def car_update(cls, data):
        query = 'UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description = %(description)s WHERE id = %(id)s'
        results = connectToMySQL('belt_schema').query_db(query, data)
        return results

    @classmethod
    def car_delete(cls, data):
        query = 'DELETE FROM cars WHERE id = %(id)s'
        results = connectToMySQL('belt_schema').query_db(query, data)
        return results

    @staticmethod
    def validate_car(data):
        is_valid = True
        query = 'SELECT * FROM cars'
        connectToMySQL('belt_schema').query_db(query, data)

        if int(data['price']) == 0:
            is_valid = False
            flash('Price needs to be greater than $0.')
        if len(data['model']) <2 or len(data['model']) > 45:
            is_valid = False
            flash('Model needs to be between 2 and 45 characters long.')
        if len(data['make']) <2 or len(data['make']) > 45:
            is_valid = False
            flash('Make needs to be between 2 and 45 characters long.')
        if int(data['year']) == 0:
            is_valid = False
            flash('Please specify the correct (YYYY) year.')
        if len(data['description']) <10 or len(data['model']) > 255:
            is_valid = False
            flash('Description needs to be between 10 and 255 characters long.')
        return is_valid