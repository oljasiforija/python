from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash


class Message:
    def __init__( self , data ):
        self.message_id = data['message_id']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id_from = data['user_id_from']
        self.user_id_send = data['user_id_send']