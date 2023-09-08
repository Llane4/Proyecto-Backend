from flask import Blueprint
from api.controllers.user_controller import UserController

user_bp = Blueprint ('user_bp', __name__)

user_bp.route('/user/<int:user_id>', methods = ['GET'])(UserController.get_user)
user_bp.route('/create_user', methods = ['POST'])(UserController.create_user)
user_bp.route('/update_user/<int:user_id>', methods = ['PUT'])(UserController.update_user)
user_bp.route('/delete_user/<int:user_id>', methods = ['DELETE'])(UserController.delete_user)
user_bp.route('/login', methods = ['POST'])(UserController.login_user)
user_bp.route('/log_out', methods = ['GET'])(UserController.log_out)