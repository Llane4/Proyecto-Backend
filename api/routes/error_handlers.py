from flask import Blueprint
from ..models.exceptions import IsNotLogged, IsNotTheOwner, NotFound


errors = Blueprint("errors", __name__)
    
@errors.app_errorhandler(IsNotLogged)
def handle_bad_request(error):
        return error.get_response()

@errors.app_errorhandler(IsNotTheOwner)
def handle_bad_request(error):
        return error.get_response()

@errors.app_errorhandler(NotFound)
def handle_bad_request(error):
        return error.get_response()

