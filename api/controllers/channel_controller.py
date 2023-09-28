from flask import jsonify, request, session 
from ..models.channels import Channel
from ..utils.session_utils import is_logged, verify_user, is_owner
from ..models.exceptions import IsNotLogged, IsNotTheOwner

class Channel_Controller:

    @classmethod
    def get_channels(cls, server_id):
        channels=Channel.get_channels(server_id)
        if channels:
            channellist=[]
            for channel in channels:
                print(channel)
                aux={
            'channel_id': channel.id,
            'name_channel': channel.name_channel,
            'owner_id': channel.owner_id,
            }
                channellist.append(aux)
            return jsonify(
        channellist), 200
        else:
            return jsonify({'message': 'No se encontraron canales'}), 404
        

    @classmethod
    def create_channel(cls):
        data = request.json
        if is_logged():
            new_channel= Channel(
                name_channel=data['name_channel'],
                owner_id=session.get('user_id')
            )
            Channel.create_channel(new_channel.name_channel, data['server_id'], new_channel.owner_id)
            return jsonify({'message': 'Canal creado exitosamente'}), 201


    @classmethod
    def delete_channel(cls, channel_id):
        result=Channel.get_channel(channel_id)
        if result is None:
            return jsonify({'error': 'No existe un server con esta ID'}), 400
        owner_id=result.owner_id
        if session['user_id']==owner_id:
            Channel.delete_channel(channel_id)
            return {}, 204
        else:
            return jsonify({'error': 'No tienes permisos para eliminar este canal'}), 400
        
    @classmethod
    def update_channel(cls):
        data=request.json
        result=Channel.get_channel(data['channel_id'])
        if result is None:
            return jsonify({'error': 'No existe un canal con esta ID'}), 400
        owner_id=result.owner_id
        if session['user_id']==owner_id:
            Channel.update_channel(data['channel_id'], data['name_channel'])
            return {}, 204
        else:
            return jsonify({'error': 'No tienes permisos para eliminar este canal'}), 400