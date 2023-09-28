from ..database import DatabaseConnection
from flask import request

class Channel:
    def __init__(self, name_channel=None, owner_id=None, id=None):
        self.name_channel=name_channel
        self.owner_id=owner_id
        self.id=id

    def get_channel(channel_id):
        query = "SELECT name_channel, owner_id, id FROM channel WHERE id=%s;"
        params = (channel_id,)
        results = DatabaseConnection.fetch_one(query, params)
        if results is not None:
            return Channel(
                name_channel=results[0],
                owner_id=results[1],
                id=results[2]
            )
        else:
            return None
    def get_channels(server_id):
        query = "SELECT name_channel, owner_id, channel_id FROM server_channel JOIN discord.channel ON discord.channel.id = discord.server_channel.channel_id WHERE server_id=%s;"
        params = (server_id,)
        results = DatabaseConnection.fetch_all(query, params)
        print(results)
        if results is not None:
            messages=[]
            for result in results:
                messages.append(
                    Channel(
                        name_channel=result[0],
                        owner_id=result[1],
                        id=result[2]
                ))

            
            return messages
            
        else:
            return None
        
    def create_channel(name_channel, server_id, owner_id):
        try:
            query= "INSERT INTO channel (name_channel, owner_id) VALUES (%s, %s) "
            params= (name_channel, owner_id)
            cursor=DatabaseConnection.get_connection().cursor()
            cursor.execute(query, params)
            channel_id = cursor.lastrowid
        except:
            print("ID DEL CANAL", channel_id)
        print("ID", channel_id)
        new_query="INSERT INTO server_channel (server_id, channel_id) VALUES(%s, %s)"
        new_params=(server_id, channel_id)
        DatabaseConnection.execute_query(new_query, new_params)

    def delete_channel(channel_id):
        query = "DELETE FROM server_channel WHERE channel_id=%s;"
        params = (channel_id ,)
        DatabaseConnection.execute_query(query, params)
        query = "DELETE FROM channel WHERE id=%s;"
        params = (channel_id ,)
        DatabaseConnection.execute_query(query, params)

    def update_channel(channel_id, name_channel):
        query= "UPDATE channel SET name_channel= %s WHERE id=%s"
        params=(name_channel, channel_id,)
        DatabaseConnection.execute_query(query, params)

    
    

