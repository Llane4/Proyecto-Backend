from flask import Blueprint
from api.controllers.message_controller import Message_Controller

message_bp = Blueprint ('message_bp', __name__)

message_bp.route('/get_messages/<int:sender_id>/<int:receiver_id>', methods = ['GET'])(Message_Controller.get_messages)
message_bp.route('/get_messages_channel/<int:receiver_id>', methods = ['GET'])(Message_Controller.get_channel_messages)
message_bp.route('/send_message', methods = ['POST'])(Message_Controller.send_message)
message_bp.route('/send_message_channel', methods = ['POST'])(Message_Controller.send_message_channel)
message_bp.route('/update_message/<int:message_id>', methods = ['PUT'])(Message_Controller.edit_message)
message_bp.route('/delete_message/<int:message_id>', methods = ['DELETE'])(Message_Controller.delete_message)