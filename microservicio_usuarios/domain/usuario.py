class Usuario:
    def __init__(self, id_usuario: int, nombre: str, email: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email

    def __repr__(self):
        return f"Usuario(id={self.id_usuario}, nombre={self.nombre}, email={self.email})"
