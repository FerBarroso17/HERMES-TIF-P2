import mysql.connector
from config import Config
import base64

class DatabaseConnection:
    _connection = None
    _config = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            print("creando conexion")
            cls._connection = mysql.connector.connect(
                host=Config.host,
                user=Config.user,
                port = Config.port,
                password = Config.password,
                database=Config.database
            )
        print("conexion exitosa")
        return cls._connection
    
    @classmethod
    def execute_query(cls, query,params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query,params)
        cls._connection.commit()
        print("query ejecutado exitosamente")
        results = cursor.fetchall()
        processed_results = []
        for result in results:
            processed_result = {}
            for i, column in enumerate(cursor.description):
                column_name = column[0]
                value = result[i]
                # Verificar si el valor es de tipo bytes (datos binarios)
                if isinstance(value, bytes):
                    # Convertir los datos binarios a base64
                    value = base64.b64encode(value).decode('utf-8')
                processed_result[column_name] = value
            processed_results.append(processed_result)

        return processed_results
    
    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query,params)
        print("fetch one ejecutado exitosamente")
        return cursor.fetchone()
    
    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query,params)
        print("fetch all ejecutado exitosamente")
        return cursor.fetchall()
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
            print("conexion cerrada exitosamente")
            
    @classmethod
    def execute_callproc(cls, procedure_name, params=None):
        cursor = cls.get_connection().cursor()
        try:
            cursor.callproc(procedure_name, params)
            cls._connection.commit()
            print("callproc ejecutado exitosamente")
            return cursor
        except mysql.connector.Error as err:
            # Manejar errores de MySQL aquí
            print(f"Error ejecutando el procedimiento almacenado: {err}")
        finally:
            cursor.close()