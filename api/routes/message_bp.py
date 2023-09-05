from flask import Blueprint
from api.controllers.message_controller import Message_Controller

message_bp = Blueprint ('message_bp', __name__)

message_bp.route('/get_messages/<int:sender_id>/<int:receiver_id>', methods = ['GET'])(Message_Controller.get_messages)
message_bp.route('/send_message', methods = ['POST'])(Message_Controller.send_message)
message_bp.route('/send_message_channel', methods = ['POST'])(Message_Controller.send_message_channel)
""" message_bp.route('/update_server/<int:server_id>', methods = ['PUT'])(ServerController.update_server)
message_bp.route('/delete_server/<int:server_id>', methods = ['DELETE'])(ServerController.delete_server) """