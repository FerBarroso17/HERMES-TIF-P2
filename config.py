from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    APP_NAME = "HERMES"

    TEMPLATE_FOLDER = "app/templates"
    STATIC_FOLDER = "app/static"
    
    SECRET_KEY = os.getenv('SECRET_KEY')
    host=os.getenv('DATABASE_HOST')
    user=os.getenv('DATABASE_USERNAME')
    port = os.getenv('DATABASE_PORT')
    password = os.getenv('DATABASE_PASSWORD')
   
    database='hermes'
