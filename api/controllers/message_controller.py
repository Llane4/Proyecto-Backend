from flask import jsonify, request
from ..models.message import Message

class Message_Controller:
    @classmethod
    def get_messages(cls, sender_id, receiver_id):
        messages=Message.get_messages(sender_id, receiver_id)
        if messages:
            messages_list=[]
            print(messages)
            
            for message in messages:
                print("USEEEEEEEEEEER",message.content)
                aux={
                    'content': message.content,
                    'send_day':message.send_day,
                }
                messages_list.append(aux)
            return jsonify(messages_list), 200
        else:
            return jsonify({'message': 'Usuario no encontrado'}), 404
        
    def get_channel_messages(cls, receiver_id):
        messages=Message.get_messages(receiver_id)
        if messages:
            messages_list=[]
            
            for message in messages:
                print("USEEEEEEEEEEER",message)
                aux={
                    'server_id': message[0].content,
                    'user_id':message[0].send_day,
                }
                messages_list.append(aux)
            return jsonify(messages_list), 200
        else:
            return jsonify({'message': 'Usuario no encontrado'}), 404    
    @classmethod    
    def send_message(cls):
        data = request.json
        new_message = Message(
            sender_id=data['sender_id'],
            receiver_id=data['receiver_id'],
            content=data['content'],
            send_day=data['send_day']
        )
        Message.send_message(new_message) 
        return jsonify({'message': 'Usuario añadido exitosamente en el servidor'}), 201 
    
    @classmethod    
    def send_message_channel(cls):
        data = request.json
        new_message = Message(
            sender_id=data['sender_id'],
            receiver_id=data['receiver_id'],
            content=data['content'],
            send_day=data['send_day']
        )
        Message.send_to_channel(new_message) 
        return jsonify({'message': 'Usuario añadido exitosamente en el servidor'}), 201 
    
    """ Borrar mensaje """
    """ Editar mensaje """