from flask import jsonify, request, session
from ..models.users import Users
from ..utils.session_utils import is_logged, verify_user
from ..models.exceptions import IsNotTheOwner, IsNotLogged, NotFound

class UserController:

    """ Funcion para conseguir la informacion de un user con su ID """
    @classmethod
    def get_user(cls):
        if is_logged():
            user_id=session.get('user_id')
            user=Users.get_user(user_id)
            if user:
                return jsonify({
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email,
                'avatar': user.avatar,
                'first_name': user.name,
                'last_name': user.lastname
            }), 200
            else:
                raise NotFound(description=f'No se encontro al usuario con el ID: {user_id}')
        else:
            raise IsNotLogged(description="No hay un usuario logeado")

    @classmethod
    def get_id(cls, email):
        user=Users.get_id(email)
        if user:
            return jsonify({
            'user_id': user.user_id,
        }), 200
        else:
            return None
        
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
        """ Agregar Error handler """
        if exist is not None:
            return jsonify({'error': 'Este correo ya esta en uso'}), 404
        else:
            Users.create_user(new_user) 
            return jsonify({'message': 'Usuario creado exitosamente'}), 201 
    
    """ Funcion para actualizar informacion de un user, falta agregar que solo se pueda actualizar la informacion propia """
    @classmethod
    def update_user(cls):
        user_id=session.get('user_id')
        user = Users.get_user(user_id)
        if not user:
            return jsonify({'message': 'Usuario no encontrado'}), 404

        data = request.json
        user.username = data.get('username', user.username) if data.get('username') is not None else user.username
        user.email = data.get('email', user.email) if data.get('email') is not None else user.email
        user.avatar = data.get('avatar', user.avatar) if data.get('avatar') is not None else user.avatar
        user.login_password = data.get('login_password', user.login_password) if data.get('login_password') is not None else user.login_password
        user.name = data.get('name', user.name) if data.get('name') is not None else user.name
        user.lastname = data.get('lastname', user.lastname) if data.get('lastname') is not None else user.lastname
        if is_logged() and verify_user(user_id):
            Users.update_user(user_id, user)
            return jsonify({'message': 'Usuario actualizado exitosamente'}), 200
        else:
            return jsonify({'error': 'No tienes los permisos para actualizar a este usuario'}), 400
    
    """ Funcion para borrar usuario con su ID """
    @classmethod
    def delete_user(cls, user_id):
        if is_logged() and verify_user(user_id):
            Users.delete_user(user_id)
            return {}, 204
        else:
            return jsonify({'error': 'No tienes los permisos para borrar a este usuario'}), 400
    """ Funcion para logear a un usuario con su username y login_password, agregar manejo de sesiones """

    @classmethod
    def login_user(cls):
        print("Intento de login")
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
            
            
            return jsonify({'error': 'Inicio de sesion con exito'})
        else: 
            return jsonify({'error': 'No se pudo iniciar sesion'}), 404
        
    @classmethod
    def log_out(cls):
        if session['email'] == "":
            raise IsNotLogged(description="No hay un usuario logeado")
        else:
            session['email']=""
            session['user_id']=""
            return jsonify({'message': 'Usuario cerro sesion exitosamente'}), 200
        
    @classmethod
    def ver_sesion(cls):
        
        if is_logged():
            sesion=session.get('email')
            id=session.get('user_id')
            return jsonify({'sesion':sesion, 'id':id})
        else:
            raise IsNotLogged(description="No hay un usuario logeado") 