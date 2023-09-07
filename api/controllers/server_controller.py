from flask import jsonify, request
from ..models.servers import Servers

class ServerController:
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
    
    @classmethod
    def delete_server(cls, server_id):
        Servers.delete_server(server_id)
        return {}, 204
    
    def add_user(cls, server_id, user_id):
        Servers.add_server(server_id, user_id)
        return {}, 200