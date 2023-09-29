from flask import jsonify, request, session
from ..models.servers import Servers
from ..utils.session_utils import is_logged, verify_user, is_owner
from ..models.exceptions import IsNotLogged, IsNotTheOwner
from .user_server_controller import User_Server_Controller

class ServerController:

    """ Funcion para conseguir la informacion de un server con su ID """
    @classmethod
    def get_server(cls, server_id):
        server=Servers.get_server(server_id)
        if server:
            return jsonify({
            'server_id': server.server_id,
            'name_server': server.name_server,
            'owner_id': server.owner_id,
            'icon': ""
        }), 200
        else:
            return jsonify({'error': 'Servidor no encontrado'}), 404

    """ Funcion para conseguir todos los servers """
    @classmethod    
    def get_servers(cls):
       
        servers=Servers.get_servers()
        if servers:
            serverlist=[]
            for server in servers: 
                aux={
            'server_id': server.server_id,
            'name_server': server.name_server,
            'owner_id': server.owner_id,
            'icon': server.icon}
                serverlist.append(aux)
            return jsonify(
        serverlist), 200
        else:
            return jsonify({'error': 'Servidor no encontrado'}), 404

    """ Funcion para crear un server, los datos de este se envian en un JSON """ 
    @classmethod
    def create_server(cls):
        data = request.json
        
        if is_logged():
            new_server = Servers(
                name_server=data['name_server'],
                owner_id=session.get('user_id'),
                icon=data['icon']
            )
            server_id=Servers.create_server(new_server) 
            return jsonify({'message': 'Servidor creado exitosamente', "id": server_id}), 201 
        else:
            raise IsNotLogged(description='No se encuentra en una sesion') 
    """ Funcion para editar un server con su ID, los datos a actualizar se envian en un JSON """
    @classmethod
    def update_server(cls, server_id):
        server = Servers.get_server(server_id)
        if not server:
            return jsonify({'message': 'Servidor no encontrado'}), 404
        data = request.json
        server.name_server = data.get('name_server', server.name_server) if data.get('name_server') is not None else server.name_server
        server.owner_id = data.get('owner_id', server.owner_id) if data.get('owner_id') is not None else server.owner_id
        server.icon = data.get('icon', server.icon) if data.get('icon') is not None else server.icon
        if is_logged(): 
            if is_owner(server.owner_id):
                Servers.update_server(server_id, server)
                return jsonify({'message': 'Servidor actualizado exitosamente'}), 200
            else:
                raise IsNotTheOwner(description='No tienes los permisos para actualizar este servidor')
        else:
            raise IsNotLogged(description='No se encuentra en una sesion')
    
    """ Funcion para eliminar un server con su ID, debe agregarse que solo el owner_id pueda borrarlo """
    @classmethod
    def delete_server(cls, server_id):
        result=Servers.get_server(server_id)
        if result is None:
            return jsonify({'error': 'No existe un server con esta ID'}), 400
        owner_id=result.owner_id
        if is_logged(): 
            if is_owner(owner_id):
                Servers.delete_server(server_id)
                return {}, 204
            else:
                raise IsNotTheOwner(description='No tienes los permisos para borrar este servidor')
        else:
            raise IsNotLogged(description='No se encuentra en una sesion')
    
    """ Funcion para que un usuario se una a un server """
    def add_user(cls, server_id, user_id):
        Servers.add_server(server_id, user_id)
        return {}, 200
    
    @classmethod
    def search_servers(cls, server_name):
        servers=Servers.search_servers(server_name)
        if servers:
            serverlist=[]
            for server in servers: 
                aux={
            'server_id': server.server_id,
            'name_server': server.name_server,
            'owner_id': server.owner_id,
            'icon': ""}
                serverlist.append(aux)
            return jsonify(
        serverlist), 200
        else:
            return jsonify({'error': 'Servidor no encontrado'}), 404