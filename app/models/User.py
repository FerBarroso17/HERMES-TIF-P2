import json
from flask import request, jsonify, redirect, url_for, render_template, session
import mysql.connector
from config import Config


class Usuario:
    def __init__(self, nombre, correo, contrasena, fecha_nacimiento, nombre_completo, apellido):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.fecha_nacimiento = fecha_nacimiento
        self.nombre_completo = nombre_completo
        self.apellido = apellido

        
    def registrar_usuario():
        data = request.json
        nombre = data.get('nombre_usuario')
        correo = data.get('correo_electronico')
        contrasena = data.get('contrasena')
        Fecha_Nac = data.get('fecha_nacimiento')
        nombre_completo = data.get('nombre')
        apellido = data.get('apellido')

        if not all([nombre, correo, contrasena, Fecha_Nac, nombre_completo, apellido]):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        insert_query = 'INSERT INTO Usuarios (nombre_usuario, correo_electronico, contrasena, fecha_nacimiento, nombre, apellido) VALUES (%s, %s, %s, %s, %s, %s)'
        insert_values = (nombre, correo, contrasena, Fecha_Nac, nombre_completo, apellido)


        try:
            cursor.execute(insert_query, insert_values)
            mysql_db.commit()
            user_id = cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error al insertar en MySQL: {err}")
            return jsonify({'error': 'Error al insertar en MySQL'}), 500

        return redirect(url_for('main.inicio')), 201
    
    def autenticar_usuario():
        data = request.json
        nombre_usuario = data.get('nombre_usuario')
        contrasena = data.get('contrasena')

        if not all([nombre_usuario, contrasena]):
            return jsonify({'error': 'Nombre de usuario y contraseña son obligatorios'}), 400

        consulta = 'SELECT usuario_id FROM Usuarios WHERE nombre_usuario = %s AND contrasena = %s'
        cursor.execute(consulta, (nombre_usuario, contrasena))
        usuario = cursor.fetchone()

        if usuario:
            session['usuario'] = nombre_usuario
            session['usuario_id'] = usuario[0]  
            print(f'Nombre de usuario en sesión: {nombre_usuario}')
            
            return jsonify({'message': 'Inicio de sesión exitoso', 'usuario': nombre_usuario}), 200
        else:
            return jsonify({'error': 'Nombre de usuario o contraseña incorrectos'}), 401

    def obtener_usuarios_json():
        try:
            with open(Usuarios_json, 'r') as archivo_json:
                contenido_json = json.load(archivo_json)
            return jsonify(contenido_json), 200
        except FileNotFoundError:
            return jsonify({'error': 'El archivo JSON no existe'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def mostrar_chatbox():
        print('Mostrando chatbox')
        if 'usuario' not in session:
            print('Usuario no autenticado en la sesión')
            return redirect(url_for('routes.mostrar_formulario_login'))
        else:
            print(f'Usuario autenticado en la sesión: {session["usuario"]}')

        return render_template('chatbox.html')

    def actualizar_usuario(usuario_id):
        data = request.json
        nuevo_nombre = data.get('nombre')
        nuevo_correo = data.get('correo')
        nueva_contrasena = data.get('contrasena')
        nueva_edad = data.get('edad')
        nuevo_nombre_completo = data.get('nombre_completo')
        nuevo_apellido = data.get('apellido')

        if not all([nuevo_nombre, nuevo_correo, nueva_contrasena, nueva_edad, nuevo_nombre_completo, nuevo_apellido]):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        update_query = 'UPDATE Usuarios SET nombre_usuario = %s, correo_electronico = %s, contrasena = %s, edad = %s, nombre = %s, apellido = %s WHERE usuario_id = %s'
        update_values = (nuevo_nombre, nuevo_correo, nueva_contrasena, nueva_edad, nuevo_nombre_completo, nuevo_apellido, usuario_id)

        try:
            cursor.execute(update_query, update_values)
            mysql_db.commit()
        except mysql.connector.Error as err:
            print(f"Error al actualizar en MySQL: {err}")
            return jsonify({'error': 'Error al actualizar en MySQL'}), 500

        contenido_actual = []

        try:
            with open(Usuarios_json, 'r') as archivo_json:
                contenido_actual = json.load(archivo_json)
        except FileNotFoundError:
            pass

        for usuario in contenido_actual:
            if usuario['Usuario'] == usuario_id:
                usuario['Datos']['nombre_usuario'] = nuevo_nombre
                usuario['Datos']['correo_electronico'] = nuevo_correo
                usuario['Datos']['contrasena'] = nueva_contrasena
                usuario['Datos']['edad'] = nueva_edad
                usuario['Datos']['nombre'] = nuevo_nombre_completo
                usuario['Datos']['apellido'] = nuevo_apellido
                break

        with open(Usuarios_json, 'w') as archivo_json:
            json.dump(contenido_actual, archivo_json, indent=4)

        return jsonify({'message': 'Usuario actualizado'}), 200
    
    def cambiar_contraseña(usuario_id):
        data = request.json
        nueva_contrasena = data.get('contrasena')
        if not all([nueva_contrasena]):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400
        update_query = 'UPDATE Usuarios SET contrasena = %s WHERE usuario_id = %s'
        update_values = (nueva_contrasena, usuario_id)
        try:
            cursor.execute(update_query, update_values)
            mysql_db.commit()
        except mysql.connector.Error as err:
            print(f"Error al actualizar en MySQL: {err}")
            return jsonify({'error': 'Error al actualizar en MySQL'}), 500
        
        contenido_actual = []

        try:
            with open(Usuarios_json, 'r') as archivo_json:
                contenido_actual = json.load(archivo_json)
        except FileNotFoundError:
            pass
        
        for usuario in contenido_actual:
            if usuario['Usuario'] == usuario_id:
                usuario['Datos']['contrasena'] = nueva_contrasena
                break
        
        with open(Usuarios_json, 'w') as archivo_json:
            json.dump(contenido_actual, archivo_json, indent=4)

        return jsonify({'message': 'Usuario actualizado'}), 200
    
Usuarios_json = 'dif carp y archivos del TIF medio uso/MAURO/HERMES - desmenuzado/data/usuarios.json'

mysql_db = mysql.connector.connect(host=Config.host,
                                    user=Config.user,
                                    password=Config.password,
                                    database=Config.database)
cursor = mysql_db.cursor()

