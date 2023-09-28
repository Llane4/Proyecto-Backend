from flask import jsonify, request, session 
from ..models.message import Message
from ..utils.session_utils import verify_user, is_logged
from ..models.exceptions import IsNotLogged, IsNotTheOwner

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
            return jsonify({'message': 'No se encontraron mensajes'}), 404
    
    """ Funcion para conseguir todos los mensajes de un canal """
    @classmethod
    def get_channel_messages(cls, receiver_id):
        print("Receiver_id", receiver_id)
        messages=Message.get_messages_channel(receiver_id)
        if messages:
            messages_list=[]
            print("MENSAJES", messages)
            for message in messages:
                aux={
                    'content': message[0].content,
                    'date':message[0].send_day,
                    'username': message[1]["username"],
                    'avatar': message[1]['avatar'],
                    'id': message[1]['id']
                }
                messages_list.append(aux)
            return jsonify(messages_list), 200
        else:
            return jsonify({'message': 'No se encontraron mensajes'}), 404  

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
        if is_logged():
            new_message = Message(
                sender_id=session.get('user_id'),
                receiver_id=data['receiver_id'],
                content=data['content']
            )
            Message.send_to_channel(new_message) 
            return jsonify({'message': 'Mensaje mandado exitosamente al canal'}), 201 
        else:
            raise IsNotLogged(description='No se encuentra en una sesion') 
    
    """ Borrar mensaje """
    @classmethod 
    def delete_message(cls, message_id):   
        sender_id=Message.get_sender_id(message_id)
        print(sender_id, session['user_id'])
        if is_logged() and verify_user(sender_id):
            Message.delete_message(message_id)
            return {}, 204
        else:
            return jsonify({"error": "No tiene permisos para borrar este mensaje"}), 404
        
    """ Borrar mensaje canales"""
    @classmethod 
    def delete_message_channel(cls, message_id):   
        sender_id=Message.get_sender_id_channel(message_id)
        print(sender_id, session['user_id'])
        if is_logged() and verify_user(sender_id):
            Message.delete_message_channel(message_id)
            return jsonify({"message": "Se borro el mensaje"}), 200
        else:
            return jsonify({"error": "No tiene permisos para borrar este mensaje"}), 404
        

    """ Editar mensaje """
    @classmethod
    def edit_message(cls, message_id):
        data = request.json
        sender_id=Message.get_sender_id(message_id)

        new_message = Message(
            sender_id="",
            receiver_id="",
            content=data['content'],
            send_day=""
        )
        if is_logged() and verify_user(sender_id):
            Message.edit_message(message_id, new_message)
            return {}, 204
        else:
            return jsonify({'error': "No tienes los permisos para editar este mensaje"}), 400

