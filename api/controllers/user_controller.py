from flask import jsonify, request
from ..models.users import Users

class UserController:
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
        Users.create_user(new_user) 
        return jsonify({'message': 'Usuario creado exitosamente'}), 201 
    
    @classmethod
    def update_user(cls, user_id):
        user = Users.get_user(user_id)
        if not user:
            return jsonify({'message': 'Usuario no encontrado'}), 404

        data = request.json
        user.username = data.get('username', user.username) if data.get('username') is not None else user.username
        user.email = data.get('email', user.email) if data.get('email') is not None else user.email
        user.login_password = data.get('login_password', user.login_password) if data.get('login_password') is not None else user.login_password
        print("PRINT USER", data)
        Users.update_user(user_id, user)
        return jsonify({'message': 'Usuario actualizado exitosamente'}), 200
    
    @classmethod
    def delete_user(cls, user_id):
        Users.delete_user(user_id)
        return {}, 204
    
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

        if result :
            return jsonify({'message': 'Usuario logeado exitosamente'}), 200
        else: 
            return jsonify({'error': 'No se pudo iniciar sesion'}), 404