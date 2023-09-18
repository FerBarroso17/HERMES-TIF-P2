from flask import Flask
from config import Config
from .routes.error_handlers import errors
from .routes.auth_bp import auth_bp
from flask_cors import CORS



def init_app():
    """Crea y configura la aplicacion Flask"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave_secreta*123'
    app.config.from_object(Config)
    app.register_blueprint(errors)
    app.register_blueprint(auth_bp)


   
    @app.route('/')
    def index():
        return '<h1>Hola Mundo</h1>'

    
    return app
