from config import Config
from flask import Flask
from flask_cors import CORS
from api.routes.user_bp import user_bp
from api.routes.server_bp import server_bp
from api.routes.user_server_bp import user_server_bp
from api.routes.message_bp import message_bp
from api.routes.channel_bp import channel_bp
from api.routes.error_handlers import errors
import os
from dotenv import load_dotenv


def init_app():
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.secret_key=(os.getenv("SECRET_KEY"))
    CORS(app , supports_credentials=True)
    app.config.from_object(Config)
    app.register_blueprint(user_bp)
    app.register_blueprint(server_bp)
    app.register_blueprint(user_server_bp)
    app.register_blueprint(message_bp)
    app.register_blueprint(channel_bp)
    app.register_blueprint(errors)
    return app