from flask import Flask, session
from config import Config
from .routes.error_handlers import errors
from .routes.blue_prints import routes_bp, main_bp
import mysql.connector



def init_app():
    """Crea y configura la aplicacion Flask"""
    app = Flask(__name__)

    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(routes_bp, url_prefix='/') 

    app.config.from_object(Config())

    mysql_db = mysql.connector.connect(
                host=Config.host,
                user=Config.user,
                password=Config.password,
                database=Config.database
                )
    
    return app
