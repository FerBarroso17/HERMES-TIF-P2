import json
from flask import request, jsonify, redirect, url_for, render_template, session
import mysql.connector
from config import Config
from datetime import datetime


class Mensajes():
    def __init__(self, mensaje_id, contenido, usuario_id, canal_id, fecha_envio):
        self.mensaje_id = mensaje_id
        self.contenido = contenido
        self.usuario_id = usuario_id
        self.canal_id = canal_id
        self.fecha_envio = fecha_envio
    
    def crear_mensaje():
        data = request.json
        contenido = data.get('contenido')
        usuario_id = data.get('usuario_id')
        canal_id = data.get('canal_id')
        fecha_envio = datetime.now()
        
        if not all([contenido, usuario_id, canal_id, fecha_envio]):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400
        
        insert_query = 'INSERT INTO Mensajes (contenido, usuario_id, canal_id, fecha_envio) VALUES (%s, %s, %s, %s)'
        insert_values = (contenido, usuario_id, canal_id, fecha_envio)
        
        try:
            cursor.execute(insert_query, insert_values)
            mysql_db.commit()
            mensaje_id = cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error al insertar en MySQL: {err}")
            return jsonify({'error': 'Error al insertar en MySQL'}), 500
        
        return jsonify({"message": "El mensaje fue creado con exito"}), 201
    
    
    def mostrar_mensajes():
        print("entro en mostrar mensaje")
        canal_id = request.args.get('canal_id')
                
        if not all([canal_id]):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400
        
        consulta = 'SELECT * FROM Mensajes WHERE canal_id = %s'
        print("llego aca")
        cursor.execute(consulta, (canal_id,))
        mensajes = cursor.fetchall()
        
        if mensajes:
            return jsonify({'mensajes': mensajes}), 200
        else:
            return jsonify({'error': 'No hay mensajes'}), 404
        
    def modificar_mensaje(mensaje_id):
        data = request.json
        contenido = data.get('contenido')
        
        if not all([contenido]):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400
        
        update_query = 'UPDATE Mensajes SET contenido = %s WHERE mensaje_id = %s'
        update_values = (contenido, mensaje_id)
        
        try:
            cursor.execute(update_query, update_values)
            mysql_db.commit()
        except mysql.connector.Error as err:
            print(f"Error al actualizar en MySQL: {err}")
            return jsonify({'error': 'Error al actualizar en MySQL'}), 500
        
        return jsonify({'message': 'Mensaje actualizado'}), 200
    
    def eliminar_mensaje(mensaje_id):
        delete_query = 'DELETE FROM Mensajes WHERE mensaje_id = %s'
        delete_values = (mensaje_id,)
        
        try:
            cursor.execute(delete_query, delete_values)
            mysql_db.commit()
        except mysql.connector.Error as err:
            print(f"Error al eliminar en MySQL: {err}")
            return jsonify({'error': 'Error al eliminar en MySQL'}), 500
        
        return jsonify({'message': 'Mensaje eliminado'}), 200



mysql_db = mysql.connector.connect(host=Config.host,
                                    user=Config.user,
                                    password=Config.password,
                                    database=Config.database)
cursor = mysql_db.cursor()
