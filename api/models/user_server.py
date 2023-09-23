from ..database import DatabaseConnection
from flask import request, session

class User_Server:
    def __init__(self, server_id=None, user_id=None):
        self.server_id=server_id
        self.user_id=user_id
    
    def get_users(server_id):
        query = """SELECT server_id, user_id, username, email FROM user_server
                   JOIN discord.user ON discord.user.id = discord.user_server.user_id
                   WHERE server_id = %s;"""
        params = (server_id,)
        results = DatabaseConnection.fetch_all(query, params)
        if results is not None:
            print("USERR", results[0][0])
            users=[]
            for result in results:
                users.append((
                    User_Server(
                        server_id=result[0],
                        user_id=result[1],
                ), {
                    'username':result[2],
                    'email': result[3]
                }))
            return users
        else:
            return None
        
    
    def add_user(new_user_in_server):
        query = "INSERT INTO user_server (user_id, server_id) VALUES (%s,%s);"
        params = (new_user_in_server.user_id, new_user_in_server.server_id)
        DatabaseConnection.execute_query(query, params)

    def get_my_servers():
        print(session['user_id'])
        query = """SELECT server_id, user_id, name_server FROM user_server
                   JOIN discord.server ON discord.server.id = discord.user_server.server_id
                   WHERE user_id = %s;"""
        params = (session['user_id'],)
        results = DatabaseConnection.fetch_all(query, params)
        if results is not None:
            print("USERR", results[0][0])
            users=[]
            for result in results:
                users.append((
                    User_Server(
                        server_id=result[0],
                        user_id=result[1],
                ), {
                    'name_server':result[2]
                    
                }))
            return users
        else:
            return None
    

        
    
    