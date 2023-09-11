from flask import Blueprint
from api.controllers.channel_controller import Channel_Controller

channel_bp = Blueprint ('channel_bp', __name__)

channel_bp.route('/get_channels/<int:server_id>', methods = ['GET'])(Channel_Controller.get_channels)
channel_bp.route('/create_channel', methods = ['POST'])(Channel_Controller.create_channel)
""" message_bp.route('/send_message_channel', methods = ['POST'])(Channel_Controller.send_message_channel) """
channel_bp.route('/update_channel', methods = ['PUT'])(Channel_Controller.update_channel)
channel_bp.route('/delete_channel/<int:channel_id>', methods = ['DELETE'])(Channel_Controller.delete_channel)