from ..database import DatabaseConnection
from flask import request
from datetime import datetime

class Message:
    def __init__(self, sender_id=None, receiver_id=None, content=None, send_day=None):
        self.sender_id=sender_id
        self.receiver_id=receiver_id
        self.content=content
        self.send_day=send_day
    
    def get_messages(sender_id, receiver_id):
        query = "SELECT content, send_day FROM message WHERE sender_id=%s AND receiver_id=%s;"
        params = (sender_id, receiver_id)
        results = DatabaseConnection.fetch_all(query, params)
        if results is not None:
            messages=[]
            for result in results:
                messages.append(
                    Message(
                        content=result[0],
                        send_day=result[1],
                ))

            print("ESTO ES ARRAY?",messages)
            return messages
            
        else:
            return None
    
    def get_messages_channel(receiver_id):
        query = """SELECT content, send_day, username, avatar, discord.channel_message.id FROM channel_message
                   JOIN discord.user ON discord.user.id = discord.channel_message.sender_id
                   WHERE receiver_id = %s;"""
        params = (receiver_id, )
        results = DatabaseConnection.fetch_all(query, params)
        if results is not None:
            messages=[]
            for result in results:
                print(result[1])
                date = str(result[1])
                messages.append((
                    Message(
                        content=result[0],
                        send_day=date
                ), {
                    'username':result[2],
                    'avatar': result[3],
                    'id': result[4]
                }))

            return messages
            
        else:
            return None

    def get_sender_id(message_id):
        query="SELECT sender_id FROM message WHERE id=%s"
        params=(message_id, )
        results=DatabaseConnection.fetch_one(query, params)
        if results is not None:
            return results[0]
            
        else:
            return None
        
    def get_sender_id_channel(message_id):
        query="SELECT sender_id FROM channel_message WHERE id=%s"
        params=(message_id, )
        results=DatabaseConnection.fetch_one(query, params)
        if results is not None:
            return results[0]
            
        else:
            return None
    def send_message(new_message):
        query = "INSERT INTO message (sender_id, receiver_id, content, send_day) VALUES (%s,%s,%s,NOW());"
        params = (new_message.sender_id, new_message.receiver_id, new_message.content)
        DatabaseConnection.execute_query(query, params)    

    def send_to_channel(new_message):
        print("ENtra aqui")
        query = "INSERT INTO channel_message (sender_id, receiver_id, content, send_day) VALUES (%s,%s,%s,NOW());"
        params = (new_message.sender_id, new_message.receiver_id, new_message.content)
        DatabaseConnection.execute_query(query, params) 

    
    def delete_message(message_id):
        query = "DELETE FROM message WHERE id=%s;"
        params = (message_id ,)
        DatabaseConnection.execute_query(query, params)

    def delete_message_channel(message_id):
        query = "DELETE FROM channel_message WHERE id=%s;"
        params = (message_id ,)
        DatabaseConnection.execute_query(query, params)

    def edit_message(message_id, content):
        query= "UPDATE message SET content=%s, edited=NOW() WHERE id=%s"
        params=(content.content, message_id,  )
        print(content.content)
        DatabaseConnection.execute_query(query, params)


