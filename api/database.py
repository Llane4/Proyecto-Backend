import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
config = {
        'host':'127.0.0.1',
        'user': os.getenv("USER"),
        'port' : "3306",
        'password': os.getenv("PASSWORD"),
        'database':'Discord'
        }



class DatabaseConnection:
    _connection = None
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                **config
            )
        return cls._connection
    
    @classmethod
    def fetch_one(cls, query, params=None):
        cursor=cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
    
    @classmethod
    def fetch_all(cls, query, params=None):
        cursor=cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    

    @classmethod
    def execute_query(cls, query, params=None):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()

    @classmethod
    def execute_query_return_id(cls, query, params=None):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)
        id=cursor._last_insert_id
        connection.commit()
        return id
        
