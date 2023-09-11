from flask import jsonify, request, session 
from ..models.message import Message

class Message_Controller:
    """ Funcion para conseguir todos los mensajes entre dos usuarios """
    @classmethod
    def get_messages(cls, sender_id, receiver_id):
        messages=Message.get_messages(sender_id, receiver_id)
        if messages:
            messages_list=[]
            for message in messages:
                aux={
                    'content': message.content,
                    'send_day':message.send_day,
                }
                messages_list.append(aux)
            return jsonify(messages_list), 200
        else:
            return jsonify({'message': 'Usuario no encontrado'}), 404
    
    """ Funcion para conseguir todos los mensajes de un canal """
    @classmethod
    def get_channel_messages(cls, receiver_id):
        messages=Message.get_messages(receiver_id)
        if messages:
            messages_list=[]
            for message in messages:
                aux={
                    'server_id': message[0].content,
                    'user_id':message[0].send_day,
                }
                messages_list.append(aux)
            return jsonify(messages_list), 200
        else:
            return jsonify({'message': 'Usuario no encontrado'}), 404  

    """ Funcion para enviar mensajes entre usuarios """  
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
    
    """ Funcion para mandar mensajes a un canal """
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
    @classmethod 
    def delete_message(cls, message_id):   
        sender_id=Message.get_sender_id(message_id)
        print(sender_id, session['user_id'])
        if(sender_id==session['user_id']):

            Message.delete_message(message_id)
            return {}, 204
        else:
            return jsonify({"error": "No tiene permisos para borrar este mensaje"}), 400
        

    """ Editar mensaje """
    @classmethod
    def edit_message(cls, message_id):
        data = request.json
        new_message = Message(
            sender_id="",
            receiver_id="",
            content=data['content'],
            send_day=""
        )
        Message.edit_message(message_id, new_message)
        return {}, 204

