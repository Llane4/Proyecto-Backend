from ..database import DatabaseConnection
from flask import request

class Servers:
    def __init__(self, server_id=None, name_server=None, owner_id=None, icon=None):
        self.server_id=server_id
        self.name_server=name_server
        self.owner_id=owner_id
        self.icon=icon
    
    def get_server(server_id):
        query = "SELECT id, name_server, owner_id, icon FROM server WHERE id = %s;"
        params = (server_id,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Servers(
                server_id=result[0],
                name_server=result[1],
                owner_id=result[2],
                icon=result[3],
            )
        else:
            return None
        
    def get_servers():
        print("LLEGA A GET SERVERS")
        query = "SELECT id, name_server, owner_id, icon FROM server;"
        results = DatabaseConnection.fetch_all(query)

        if results is not None:
            
            users=[]
            for result in results:
                users.append((
                    Servers(
                server_id=result[0],
                name_server=result[1],
                owner_id=result[2],
                icon=result[3],
            )))
            return users
        else:
            return None
        
    def create_server(server):
        query = "INSERT INTO server (name_server, owner_id, icon) VALUES (%s,%s,%s);"
        params = (server.name_server, server.owner_id, server.icon)
        id = DatabaseConnection.execute_query_return_id(query, params)
        return id

    def update_server(server_id, server):
        query= "UPDATE server SET name_server= %s, owner_id=%s, icon=%s WHERE id=%s"
        params= (server.name_server, server.owner_id, server.icon, server_id)
        DatabaseConnection.execute_query(query, params)

    def delete_server(server_id):
        query = "DELETE FROM Server WHERE id=%s;"
        params = (server_id ,)
        DatabaseConnection.execute_query(query, params)

    def add_user(server_id, user_id):
        user= ""

    def search_servers(server_name):
        query = f"SELECT id, name_server, owner_id, icon FROM server WHERE name_server LIKE '%{server_name}%';"
        results = DatabaseConnection.fetch_all(query)

        if results is not None:
            
            users=[]
            for result in results:
                users.append((
                    Servers(
                server_id=result[0],
                name_server=result[1],
                owner_id=result[2],
                icon=result[3],
            )))
            return users
        else:
            return None