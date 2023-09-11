from flask import jsonify, request, session
from ..models.users import Users

class UserController:

    """ Funcion para conseguir la informacion de un user con su ID """
    @classmethod
    def get_user(cls, user_id):
        user=Users.get_user(user_id)
        if user:
            return jsonify({
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email
        }), 200
        else:
            return jsonify({'message': 'Usuario no encontrado'}), 404

    @classmethod
    def get_id(cls, email):
        user=Users.get_id(email)
        if user:
            return jsonify({
            'user_id': user.user_id,
        }), 200
        else:
            return jsonify({'message': 'Usuario no encontrado'}), 404
        
    """ Funcion para crear un user, los datos de este se envian en un JSON, agregar verificacion de si ya existe un user con el email enviado """
    @classmethod
    def create_user(cls):
        data = request.json
        new_user = Users(
            username=data['username'],
            email=data['email'],
            login_password=data['login_password'],
            name=data['name'],
            lastname=data['lastname'],
            birthday=data['birthday']
        )
        exist=Users.get_id(new_user.email)
        if exist is not None:
            return jsonify({'message': 'Este correo ya esta en uso'}), 404
        else:
            Users.create_user(new_user) 
            return jsonify({'message': 'Usuario creado exitosamente'}), 201 
    
    """ Funcion para actualizar informacion de un user, falta agregar que solo se pueda actualizar la informacion propia """
    @classmethod
    def update_user(cls, user_id):
        user = Users.get_user(user_id)
        if not user:
            return jsonify({'message': 'Usuario no encontrado'}), 404

        data = request.json
        user.username = data.get('username', user.username) if data.get('username') is not None else user.username
        user.email = data.get('email', user.email) if data.get('email') is not None else user.email
        user.login_password = data.get('login_password', user.login_password) if data.get('login_password') is not None else user.login_password
        Users.update_user(user_id, user)
        return jsonify({'message': 'Usuario actualizado exitosamente'}), 200
    
    """ Funcion para borrar usuario con su ID """
    @classmethod
    def delete_user(cls, user_id):
        Users.delete_user(user_id)
        return {}, 204
    
    """ Funcion para logear a un usuario con su username y login_password, agregar manejo de sesiones """
    @classmethod
    def login_user(cls):
        data=request.json
        user=Users(
            username="",
            email=data['email'],
            login_password=data['login_password'],
            name="",
            lastname="",
            birthday=""
        )
        result=Users.login_user(user)
        """ Agregar manejo de errores """
        if result :
            user_id=Users.get_id(user.email)
            session['email']=user.email
            session['user_id']=user_id.user_id
            return jsonify({'message': f'Usuario logeado exitosamente'}), 200
        else: 
            return jsonify({'error': 'No se pudo iniciar sesion'}), 404
        
    @classmethod
    def log_out(cls):
        if session['email'] == "":
            return jsonify({'error': 'No hay un usuario logeado'}), 404
        else:
            session['email']=""
            session['user_id']=""
            return jsonify({'message': 'Usuario cerro sesion exitosamente'}), 200