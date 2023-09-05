from ..database import DatabaseConnection
from flask import request

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
        
    def send_message(new_message):
        query = "INSERT INTO message (sender_id, receiver_id, content, send_day) VALUES (%s,%s,%s,NOW());"
        params = (new_message.sender_id, new_message.receiver_id, new_message.content)
        DatabaseConnection.execute_query(query, params)    

    def send_to_channel(new_message):
        print("ENtra aqui")
        query = "INSERT INTO channel_message (sender_id, receiver_id, content, send_day) VALUES (%s,%s,%s,NOW());"
        params = (new_message.sender_id, new_message.receiver_id, new_message.content)
        DatabaseConnection.execute_query(query, params) 

        