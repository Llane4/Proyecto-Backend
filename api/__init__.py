from config import Config
from flask import Flask
from flask_cors import CORS
from api.routes.user_bp import user_bp
from api.routes.server_bp import server_bp
from api.routes.user_server_bp import user_server_bp
from api.routes.message_bp import message_bp

def init_app():
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    app.register_blueprint(user_bp)
    app.register_blueprint(server_bp)
    app.register_blueprint(user_server_bp)
    app.register_blueprint(message_bp)
    CORS(app)
    return app