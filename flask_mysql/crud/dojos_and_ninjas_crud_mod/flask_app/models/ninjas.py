from flask_app.config.mysqlconnection import connectToMySQL

class Ninjas:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data ['last_name']
        self.age = data ['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = []

    @classmethod   
    def add_ninja(cls, data):
        query = "INSERT INTO ninjas (dojo_id,first_name, last_name, age, created_at, updated_at) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW() )"
        connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    
    # @classmethod
    # def get_all_ninjas(cls, data):
    #     query = "SELECT * FROM ninjas WHERE 'dojo_id = %(dojo_id)s"
    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    #     ninja = []
    #     for ninja in results:
    #         ninja.append(cls(ninja))
    #     return ninja
