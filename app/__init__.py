from flask import Flask
from config import Config


def init_app():
    """Crea y configura la aplicacion Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
   
    @app.route('/')
    def index():
        return '<h1>Hola Mundo</h1>'

    
    return app
