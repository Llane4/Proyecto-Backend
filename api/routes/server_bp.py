from flask import Blueprint
from api.controllers.server_controller import ServerController

server_bp = Blueprint ('server_bp', __name__)

server_bp.route('/server/<int:server_id>', methods = ['GET'])(ServerController.get_server)
server_bp.route('/servers', methods = ['GET'])(ServerController.get_servers)
server_bp.route('/create_server', methods = ['POST'])(ServerController.create_server)
server_bp.route('/update_server/<int:server_id>', methods = ['PUT'])(ServerController.update_server)
server_bp.route('/delete_server/<int:server_id>', methods = ['DELETE'])(ServerController.delete_server)