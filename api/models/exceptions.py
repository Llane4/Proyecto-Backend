from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    
class IsNotLogged(CustomException):
        def __init__(self, description):
            super().__init__(status_code=404, name="Is Not Logged", description=description)
            self.description=description
    
class IsNotTheOwner(CustomException):
        def __init__(self, description):
            super().__init__(status_code=400, name="User is not the Owner", description=description)
            self.description= description

class NotFound(CustomException):
        def __init__(self, description):
            super().__init__(status_code=400, name="Not Found", description=description)
            self.description= description

            