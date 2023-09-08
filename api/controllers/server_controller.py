from flask import jsonify, request, session
from ..models.servers import Servers

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
            return jsonify({'message': 'Servidor no encontrado'}), 404

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
            'icon': ""}
                serverlist.append(aux)
            return jsonify(
        serverlist), 200
        else:
            return jsonify({'message': 'Servidor no encontrado'}), 404

    """ Funcion para crear un server, los datos de este se envian en un JSON """ 
    @classmethod
    def create_server(cls):
        data = request.json
        new_server = Servers(
            name_server=data['name_server'],
            owner_id=data['owner_id'],
            icon=data['icon']
        )
        Servers.create_server(new_server) 
        return jsonify({'message': 'Servidor creado exitosamente'}), 201 
    
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
        print("PRINT USER", data)
        Servers.update_server(server_id, server)
        return jsonify({'message': 'Servidor actualizado exitosamente'}), 200
    
    """ Funcion para eliminar un server con su ID, debe agregarse que solo el owner_id pueda borrarlo """
    @classmethod
    def delete_server(cls, server_id):
        result=Servers.get_server(server_id)
        if result is None:
            return jsonify({'error': 'No existe un server con esta ID'}), 400
        owner_id=result.owner_id
        if session['user_id']==owner_id:
            Servers.delete_server(server_id)
            return {}, 204
        else:
            return jsonify({'error': 'No tienes permisos para eliminar este server'}), 400
    
    """ Funcion para que un usuario se una a un server """
    def add_user(cls, server_id, user_id):
        Servers.add_server(server_id, user_id)
        return {}, 200