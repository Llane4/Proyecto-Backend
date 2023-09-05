from ..database import DatabaseConnection
from flask import request

class Users:
    def __init__(self, user_id=None, username=None, email=None, login_password=None, avatar=None, name=None, lastname=None, birthday=None):
        self.user_id=user_id
        self.username=username
        self.email=email
        self.login_password=login_password
        self.avatar=avatar
        self.name=name
        self.lastname=lastname
        self.birthday=birthday

    def get_user(user_id):
        query = "SELECT id, username, email, login_password, avatar, name, lastname, birthday FROM user WHERE id = %s;"
        params = (user_id,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Users(
                user_id=result[0],
                username=result[1],
                email=result[2],
                login_password=result[3],
                avatar=result[4],
                name=result[5],
                lastname=result[6],
                birthday=result[7],
            )
        else:
            return None
        
    
    def create_user(user):
        query = "INSERT INTO user (username, email, login_password, name, lastname, birthday) VALUES (%s,%s,%s, %s, %s, %s);"
        params = (user.username, user.email, user.login_password, user.name, user.lastname, user.birthday)
        DatabaseConnection.execute_query(query, params)

    def update_user(user_id, user):
        query= "UPDATE user SET username= %s, email=%s, login_password=%s, name=%s, lastname=%s, birthday=%s WHERE id=%s"
        params= (user.username, user.email, user.login_password,user.name, user.lastname, user.birthday ,user_id)
        DatabaseConnection.execute_query(query, params)

    def delete_user(user_id):
        query = "DELETE FROM user WHERE id=%s;"
        params = (user_id ,)
        DatabaseConnection.execute_query(query, params)