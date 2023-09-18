from ..database import DatabaseConnection  


class UsuarioModel:

    def __init__(self, **kwargs):
        self.usuario_id = kwargs.get('usuario_id')
        self.nombre_usuario = kwargs.get('nombre_usuario')
        self.correo_electronico = kwargs.get('correo_electronico')
        self.contrasena = kwargs.get('contrasena')
        self.foto_perfil = kwargs.get('foto_perfil')

    # Toma los datos del usuario y los convierte en un formato serializado
    def serialize(self):
        return {
            "usuario_id": self.usuario_id,
            "nombre_usuario": self.nombre_usuario,
            "correo_electronico": self.correo_electronico,
            "contrasena": self.contrasena,
            "foto_perfil": self.foto_perfil 
        }

    @classmethod
    def get_usuario(cls, usuario):
        print("llamando a get_usuario")
        try:
            query = "SELECT * FROM usuarios WHERE usuario_id = %s"
            params = (usuario.usuario_id,)
            result = DatabaseConnection.fetch_one(query, params)
            if result is not None:
                usuario = cls(
                    usuario_id=result[0],  # Índice 0 corresponde a usuario_id
                    nombre_usuario=result[1],       # Índice 1 corresponde a nombre_usuario
                    correo_electronico=result[2],       # Índice 2 corresponde a correo_electronico
                    contrasena=result[3],   # Índice 3 corresponde a contrasena
                    foto_perfil=result[4]  # Índice 4 corresponde a foto_perfil
                    )
                return usuario
            
            return None
        except Exception as e:
            # Captura la excepción y devuelve un diccionario con el código de error y la descripción
            return {"error_code": 500, "error_description": str(e)}
        finally:
            DatabaseConnection.close_connection()
    
    @classmethod
    def is_registered(cls,usuario):

        query = """SELECT usuario_id FROM usuarios WHERE correo_electronico = %s AND contrasena = %s"""

        params = (usuario.correo_electronico, usuario.contrasena)

        result = DatabaseConnection.fetch_one(query,params=params)

        if result is not None:
            return True
        return False
    
    
    @classmethod
    def create(cls, usuario_id):
        """Crear un nuevo usuario
        Args:
            - usuario (Usuario): Objeto de usuario
        """
        query = """INSERT INTO usuarios (nombre_usuario, correo_electronico, contrasena) 
                   VALUES (%s, %s, %s)"""

        params = usuario_id.nombre_usuario, usuario_id.correo_electronico, usuario_id.contrasena
        DatabaseConnection.execute_query(query, params=params)
        # Después de la inserción, obtén el id_usuario_id del registro recién creado
        query = "SELECT LAST_INSERT_ID()"
        result = DatabaseConnection.fetch_one(query)
        if result is not None:
            return result[0]  # devuelve el usuario_id
        else:
            return None
    
    @classmethod
    def correo_existente(cls, usuario):
        """Verificar si un correo_electronico electrónico existe en la base de datos.
        Args:
            - correo_electronico (str): Correo_electronico electrónico a verificar
        Returns:
            - bool: True si el correo_electronico existe, False si no existe o si hay un error
        """
        query = "SELECT COUNT(*) FROM usuarios WHERE correo_electronico = %s"
        params = (usuario.correo_electronico,)

        try:
            result = DatabaseConnection.fetch_one(query, params)

            if result is not None and result[0] > 0 :
                return True
            else:
                return False
        except Exception as e:
            # Manejo de errores: puedes registrar el error o realizar otras acciones según tus necesidades
            print(f"Error al verificar el correo_electronico electrónico: {str(e)}")
            return False
    

    @classmethod
    def update(cls, usuario_id):
        """Actualizar un usuario
        Args:
            - usuario (Usuario): Objeto de usuario
        """
        columnas_permitidas = {'nombre_usuario', 'correo_electronico', 'contrasena'}
        query_parts = []
        params = []
        for key, value in usuario_id.__dict__.items():
            if key in columnas_permitidas and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(usuario_id.usuario_id)

        query = "UPDATE usuarios SET " + ", ".join(query_parts) + " WHERE usuario_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def exists(cls, usuario_id):
        try:
            query = "SELECT COUNT(*) FROM usuarios WHERE usuario_id = %s"
            params = (usuario_id,)
            result = DatabaseConnection.fetch_one(query, params)

            if result and result[0] > 0:
                return True
            else:
                return False
        except Exception as e:
            return False

    @classmethod
    def delete(cls, usuario_id):
        """Eliminar un usuario
        Args:
            - usuario_id (int): ID del usuario a eliminar
        """
        query = "DELETE FROM usuarios WHERE usuario_id = %s"
        params = (usuario_id,)
        DatabaseConnection.execute_query(query, params=params)
    




# # Crear un nuevo usuario
# Fer = UsuarioModel(nombre_usuario='Fernando Barroso', correo_electronico='fb@gmail.com', contrasena='anda951*')
# UsuarioModel.create(Fer) # Devolverá el id_usuario_id del registro recién creado

# # Verificar si el correo  ya existe en la base de datos
# print(UsuarioModel.correo_existente(Fer))  # Devolverá True

# # Obtener los datos de la base de datos
# Fer_db = UsuarioModel.get_usuario(Fer)
# print(Fer_db.serialize())  # Imprimirá los datos de Fer