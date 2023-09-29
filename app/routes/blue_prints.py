from flask import Blueprint, render_template, session
from ..models.User import Usuario
from ..models.Servidores import Servidores
from ..models.Mensajes import Mensajes
from ..models.Canales import Canales

routes_bp = Blueprint('routes', __name__) 
main_bp = Blueprint('main', __name__) 

@main_bp.route('/')
def inicio():
    return render_template('portada.html')

@routes_bp.route('/register', methods=['GET'])
def mostrar_formulario_registro():
    return render_template('register.html')

@routes_bp.route('/login', methods=['GET'])
def mostrar_formulario_login():
    return render_template('login.html')

@routes_bp.route('/chatbox')
def mostrar_chatbox():
    print("entro en BP")
    return Usuario.mostrar_chatbox()

@routes_bp.route('/usuarios-json', methods=['GET'])
def obtener_usuarios_json():
    return Usuario.obtener_usuarios_json()

@routes_bp.route('/usuarios', methods=['POST'])
def registrar_usuario():
    return Usuario.registrar_usuario()

@routes_bp.route('/usuarios/login', methods=['POST'])
def autenticar_usuario():
    return Usuario.autenticar_usuario()

@routes_bp.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    return Usuario.actualizar_usuario(usuario_id)

@routes_bp.route('/usuarios/contraseña/<int:usuario_id>', methods=['PUT'])
def cambiar_contraseña(usuario_id):
    return Usuario.cambiar_contraseña(usuario_id)

"""Servidores"""

@routes_bp.route('/procesar_formulario', methods=['POST'])
def crear_servidor():
    return Servidores.crear_servidor()

@routes_bp.route('/obtener_servidores', methods=['GET'])
def obtener_servidores_usuario():
    return Servidores.obtener_servidores_usuario()

@routes_bp.route('/servidores', methods=['GET'])
def mostrar_todos_servidores():
    return Servidores.mostrar_todos_servidores()

"""Canales"""

@routes_bp.route('/servidores/<int:servidor_id>/canales', methods=['POST'])
def crear_canal_servidor(servidor_id):
    return Canales.crear_canal(servidor_id)

@routes_bp.route('/servidores/<int:servidor_id>/canales', methods=['GET'])
def obtener_canales_servidor(servidor_id):
    return Canales.obtener_canales_servidor(servidor_id)

@routes_bp.route('/Canales', methods=['GET'])
def crear_canal():
    return render_template('canales.html')

"""Mensajes"""

@routes_bp.route('/mensajes', methods=['POST'])
def crear_mensaje():
    return Mensajes.crear_mensaje()

@routes_bp.route('/mensajes', methods=['GET'])
def mostrar_mensajes():
    return Mensajes.mostrar_mensajes()

@routes_bp.route('/mensajes/<int:mensaje_id>', methods=['PUT'])
def modificar_mensaje(mensaje_id):
    return Mensajes.modificar_mensaje(mensaje_id)

@routes_bp.route('/mensajes/<int:mensaje_id>', methods=['DELETE'])
def eliminar_mensaje(mensaje_id):
    return Mensajes.eliminar_mensaje(mensaje_id)

@routes_bp.route('/mensajesht', methods=['GET'])
def ir_mensajes():
    return render_template('mensajes.html')
