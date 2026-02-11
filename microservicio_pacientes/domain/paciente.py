class Paciente:
    def __init__(self, id_paciente: int, nombre: str, email: str):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.email = email

    def __repr__(self):
        return f"Paciente(id={self.id_paciente}, nombre={self.nombre}, email={self.email})"
