from flask_app.config.mysqlconnection import connectToMySQL
from .ninjas import Ninjas


class Dojos:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append (cls(dojo) )
        return dojos

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW() )"
        connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def single_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(dojo_id)s ;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print (results)
        dojo = cls(results[-1])
        for row in results:
            ninja = {
                'id' :row['id'],
                'first_name' :row['first_name'],
                'last_name' :row ['last_name'],
                'age' :row ['age'],
                'created_at' :row['ninjas.created_at'],
                'updated_at' :row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninjas(ninja))
        return dojo

        


