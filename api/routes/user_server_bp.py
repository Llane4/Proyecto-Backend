from flask import Blueprint
from api.controllers.user_server_controller import User_Server_Controller

user_server_bp = Blueprint ('user_server_bp', __name__)

user_server_bp.route('/get_users/<int:server_id>', methods = ['GET'])(User_Server_Controller.get_users)
user_server_bp.route('/add_user', methods = ['POST'])(User_Server_Controller.add_user)
""" user_server_bp.route('/update_user/<int:user_id>', methods = ['PUT'])(User_Server.update_user)
user_server_bp.route('/delete_user/<int:user_id>', methods = ['DELETE'])(User_Server.delete_user) """