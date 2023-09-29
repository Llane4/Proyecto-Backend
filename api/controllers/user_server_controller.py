from flask import jsonify, request, session
from ..models.user_server import User_Server
from ..utils.session_utils import is_logged, verify_user
from ..models.exceptions import IsNotTheOwner, IsNotLogged, NotFound

class User_Server_Controller:
    @classmethod
    def get_users(cls, server_id):
        users=User_Server.get_users(server_id)
        if users:
            user_list=[]
            
            for user in users:
              
                aux={
                    'server_id': user[0].server_id,
                    'user_id':user[0].user_id,
                    'username': user[1]['username'],
                    'email': user[1]['email']
                }
                user_list.append(aux)
            return jsonify(user_list), 200
        else:
            return jsonify({'message': 'Usuario no encontrado'}), 404
    @classmethod    
    def add_user(cls):
        data = request.json
        if is_logged():
            new_user_in_server = User_Server(
                server_id=data['server_id'],
                user_id=session.get('user_id')
            )
            exist=User_Server.get_user(new_user_in_server)
            
            if exist== False:                
                return jsonify({'error': 'No se pudo añadir al usuario'}), 400
            else:
                User_Server.add_user(new_user_in_server) 
                return jsonify({'message': 'Usuario añadido exitosamente en el servidor'}), 201
        else:
            return jsonify({'error': 'El usuario no fue añadido al servidor'}), 400 
    
    @classmethod
    def get_my_servers(cls):
        
        if is_logged(): 
            users=User_Server.get_my_servers()
            if users:
                user_list=[]
            
                for user in users:
                    
                    aux={
                        'server_id': user[0].server_id,
                        'user_id':user[0].user_id,
                        'name_server': user[1]['name_server'],
                        'icon':user[1]['icon']
                    }
                    user_list.append(aux)
                return jsonify(user_list), 200
            else:
                return jsonify({'error': 'No se encontraron servidores'}), 404
        else:
            raise IsNotLogged(description='No se encuentra en una sesion')
        