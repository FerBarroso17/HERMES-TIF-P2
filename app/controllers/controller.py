from ..models import UsuarioModel
from flask import request, session, jsonify, render_template, url_for, redirect
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

        if UsuarioModel.correo_existente(usuario):
            return jsonify({'message': 'El correo ya está registrado'}), 400
        else:    
            
            usuario_id_creado = UsuarioModel.create(usuario)

            if usuario_id_creado is not None:
                return jsonify({'message': 'Usuario creado exitosamente', 'usuario_id': usuario_id_creado}), 201
            else:
                 return jsonify({'message': 'No se pudo crear el usuario'}), 500
            
    @classmethod
    def get_user(cls, usuario_id):
        print("llamando a get_user")
        user = UsuarioModel(usuario_id=usuario_id)
    
        result = UsuarioModel.get_usuario(user)
    
        if isinstance(result, dict) and 'error_code' in result:
             return jsonify({'message': 'Error: ' + result['error_description']}), result['error_code']
    
        if result is not None:
            processed_result = result.serialize()
            if isinstance(processed_result.get('foto_perfil'), bytes):
                processed_result['foto_perfil'] = base64.b64encode(processed_result['foto_perfil']).decode('utf-8')
            return jsonify(processed_result), 200
        return jsonify({'message': 'usuario_id no existe'}), 404
    
    
