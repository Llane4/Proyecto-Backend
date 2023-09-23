import os
from dotenv import load_dotenv


class Config:
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    SECRET_KEY='123545'
    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"