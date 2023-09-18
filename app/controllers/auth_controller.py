from ..models.UsuarioModels import UsuarioModel
from flask import request, session, jsonify
import base64

class UsuarioController:
    @classmethod
    def login(cls):
        data = request.json
        usuario = UsuarioModel(
            correo_electronico = data.get('correo_electronico'),
            contrasena = data.get('contrasena')
        )
        
        if UsuarioModel.is_registered(usuario):
            session['correo_electronico'] = data.get('correo_electronico')
           
            return {"message": "Sesion iniciada exitosamente"},200
        else:
            return {"message": "Correo o contrasena incorrecta"},401
    
    @classmethod
    def logout(cls):
        session.pop('correo_electronico', None)
        return {"message": "Sesion cerrada"}, 200 
    
    @classmethod
    def crear_usuario(cls):
        data = request.json
        usuario = UsuarioModel(**data)

        # Verificar si el correo ya existe en la base de datos
        if UsuarioModel.correo_existente(usuario):
            # El correo ya existe en la base de datos, devuelve un mensaje de error
            return jsonify({'message': 'El correo ya está registrado'}), 400
        else:    
            
            usuario_id_creado = UsuarioModel.create(usuario)

            if usuario_id_creado is not None:
                 # Si se creó el usuario exitosamente, devuelve una respuesta con el ID del usuario creado
                return jsonify({'message': 'Usuario creado exitosamente', 'usuario_id': usuario_id_creado}), 201
            else:
                 # En caso de error
                 return jsonify({'message': 'No se pudo crear el usuario'}), 500
            
    @classmethod
    def get_user(cls, usuario_id):
        print("llamando a get_user")
        user = UsuarioModel(usuario_id=usuario_id)
    
        result = UsuarioModel.get_usuario(user)
    
        if isinstance(result, dict) and 'error_code' in result:
            # Si result es un diccionario con error_code, significa que se produjo un error
             return jsonify({'message': 'Error: ' + result['error_description']}), result['error_code']
    
        if result is not None:
            # Procesa los datos binarios antes de incluirlos en la respuesta JSON
            processed_result = result.serialize()
            # Verifica si 'foto_perfil' es una cadena de bytes
            if isinstance(processed_result.get('foto_perfil'), bytes):
                # Convierte los bytes en una cadena base64
                processed_result['foto_perfil'] = base64.b64encode(processed_result['foto_perfil']).decode('utf-8')
            return jsonify(processed_result), 200
        return jsonify({'message': 'usuario_id no existe'}), 404
    
