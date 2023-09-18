from dotenv import dotenv_values

class Config:
    # config = dotenv_values(".env")
    
    # print(config)
    # SECRET_KEY = config['SECRET_KEY']
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    APP_NAME = "HERMES"

    TEMPLATE_FOLDER = "app/templates"
    STATIC_FOLDER = "app/static"
    
    # host=config['DATABASE_HOST']
    # user=config['DATABASE_USERNAME']
    # port = config['DATABASE_PORT']
    # password = config['DATABASE_PASSWORD']

    host='127.0.0.1'
    user='Fernando'
    port = '3306'
    password = 'Hastalax6*&'
    database='hermes'
