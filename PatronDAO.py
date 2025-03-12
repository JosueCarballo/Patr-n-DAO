import mysql.connector

# Modelo (Representa la estructura de datos)
class Usuario:
    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo

# DAO (Data Access Object)
class UsuarioDAO:
    def __init__(self, host="localhost", port=3307, user="root", password="", database="usuarios_db"):
        self.conexion = mysql.connector.connect(
            host=host,
            port=3308,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexion.cursor()

    # Create
    def insertar_usuario(self, usuario):
        self.cursor.execute(
            "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)",
            (usuario.nombre, usuario.correo)
        )
        self.conexion.commit()
        print(f"Usuario '{usuario.nombre}' insertado correctamente.")

    # Read
    def obtener_usuario(self, id_usuario):
        self.cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id_usuario,))
        datos = self.cursor.fetchone()
        if datos:
            print(f"🔍 Usuario encontrado: ID: {datos[0]}, Nombre: {datos[1]}, Correo: {datos[2]}")
            return Usuario(*datos)
        print("Usuario no encontrado.")
        return None

    # Update
    def actualizar_usuario(self, usuario):
        self.cursor.execute(
            "UPDATE usuarios SET nombre = %s, correo = %s WHERE id = %s",
            (usuario.nombre, usuario.correo, usuario.id_usuario)
        )
        self.conexion.commit()
        print(f"Usuario con ID {usuario.id_usuario} actualizado correctamente.")

    # Delete
    def eliminar_usuario(self, id_usuario):
        self.cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        self.conexion.commit()
        print(f"Usuario con ID {id_usuario} eliminado correctamente.")

    # Mostrar todos los usuarios
    def mostrar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        usuarios = [Usuario(*fila) for fila in self.cursor.fetchall()]
        if usuarios:
            print("\nLista de usuarios:")
            for usuario in usuarios:
                print(f"ID: {usuario.id_usuario}, Nombre: {usuario.nombre}, Correo: {usuario.correo}")
        else:
            print("📭 No hay usuarios registrados.")
        return usuarios

    # Cerrar conexión
    def cerrar_conexion(self):
        self.conexion.close()
        print("🔒 Conexión cerrada correctamente.")

# Ejemplo de uso
if __name__ == "__main__":
    dao = UsuarioDAO()

    # Insertar usuarios
    dao.insertar_usuario(Usuario(None, "Oscar Avilez", "oscar@gmail.com"))
    dao.insertar_usuario(Usuario(None, "Hugo Osorio", "hugo@gmail.com"))
    dao.insertar_usuario(Usuario(None, "Omar Cab", "omar@gmail.com"))

    # Leer y mostrar usuarios
    dao.mostrar_usuarios()

    # Obtener un usuario específico
    dao.obtener_usuario(8)

    # Actualizar un usuario
    usuario_actualizado = Usuario(7, "Lapincs Balan", "lapincsfuentes@gmail.com")
    dao.actualizar_usuario(usuario_actualizado)

    # Eliminar un usuario
    dao.eliminar_usuario(9)

    # Mostrar usuarios actualizados
    dao.mostrar_usuarios()

    dao.cerrar_conexion()
