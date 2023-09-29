from datetime import datetime
import json
from flask import request, jsonify, redirect, url_for, render_template, session
import mysql.connector
from config import Config


mysql_db = mysql.connector.connect(host=Config.host,
                                    user=Config.user,
                                    password=Config.password,
                                    database=Config.database)
cursor = mysql_db.cursor()

class Canales:
    def __init__(self, canal_id, nombre_canal, servidor_id, propietario_id):
        self.canal_id = canal_id
        self.nombre_canal = nombre_canal
        self.servidor_id = servidor_id
        self.propietario_id = propietario_id

    def crear_canal(servidor_id):
        data = request.json
        nombre_canal = data.get('nombre_canal')
        propietario_id = data.get('propietario_id')

        if not all([nombre_canal, propietario_id]):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        insert_query = 'INSERT INTO Canales (nombre_canal, servidor_id, propietario_id) VALUES (%s, %s, %s)'
        insert_values = (nombre_canal, servidor_id, propietario_id)

        try:
            cursor.execute(insert_query, insert_values)
            mysql_db.commit()
            canal_id = cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error al insertar en MySQL: {err}")
            return jsonify({'error': 'Error al insertar en MySQL'}), 500

        return jsonify({'message': 'Canal creado'}), 201
    
    def obtener_canales_servidor(servidor_id):
        consulta = 'SELECT * FROM Canales WHERE servidor_id = %s'
        cursor.execute(consulta, (servidor_id,))
        canales = cursor.fetchall()
        
        if canales:
            return jsonify({'canales': canales}), 200, print("canales:", canales)
             
        else:
            return jsonify({'error': 'No hay canales'}), 404
    
    




