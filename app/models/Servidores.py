from datetime import datetime
import json
from flask import request, jsonify, redirect, url_for, render_template, session
import mysql.connector
from config import Config


class Servidores:
    def __init__(self, servidor_id, nombre_servidor, descripcion, fecha_creacion, propietario_id, foto_servidor):
        self.servidor_id = servidor_id
        self.nombre_servidor = nombre_servidor
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.propietario_id = propietario_id
        self.foto_servidor = foto_servidor
    
    def crear_servidor():
        data = request.json
        print("data:", data)
        server_name = data.get("serverName")
        server_description = data.get("serverDescription")

        if 'usuario_id' in session:
            server_id = session['usuario_id']
        else:
            return jsonify({'error': 'Usuario no autenticado'}), 401

        print("server_name:", server_name)
        print("server_description:", server_description)
        print("server_id:", server_id)

        if not all([server_name, server_description, server_id]):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        foto_servidor = request.files.get("foto_servidor")

        insert_query = 'INSERT INTO Servidores (nombre_servidor, descripcion, propietario_id) VALUES (%s, %s, %s)'
        insert_values = (server_name, server_description, server_id)

        try:
            cursor.execute(insert_query, insert_values)
            mysql_db.commit()
            servidor_id = cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error al insertar en MySQL: {err}")
            return jsonify({'error': 'Error al insertar en MySQL'}), 500


        return jsonify({'message': 'Servidor creado'}), 201
    
    def obtener_servidores_usuario():
        try:
            if 'usuario_id' not in session:
                return jsonify({'error': 'Usuario no autenticado'}), 401

            usuario_id = session['usuario_id']

            consulta = 'SELECT servidor_id, nombre_servidor FROM Servidores WHERE propietario_id = %s'
            cursor.execute(consulta, (usuario_id,))
            servidores = cursor.fetchall()

            lista_servidores = [{'servidor_id': servidor[0], 'nombre_servidor': servidor[1]} for servidor in servidores]

            return jsonify({'servidores': lista_servidores}), 200
        except mysql.connector.Error as err:
            print(f"Error al obtener servidores: {err}")
            return jsonify({'error': 'Error al obtener servidores'}), 500
        
    def mostrar_todos_servidores():
        try:
            consulta = 'SELECT * FROM Servidores'
            cursor.execute(consulta)
            servidores = cursor.fetchall()

            lista_servidores = [{'servidor_id': servidor[0], 'nombre_servidor': servidor[1]} for servidor in servidores]
            print("lista_servidores:", lista_servidores)
            
            return jsonify({'servidores': lista_servidores}), 200
        except mysql.connector.Error as err:
            print(f"Error al obtener servidores: {err}")
            return jsonify({'error': 'Error al obtener servidores'}), 500


mysql_db = mysql.connector.connect(host=Config.host,
                                    user=Config.user,
                                    password=Config.password,
                                    database=Config.database)
cursor = mysql_db.cursor()