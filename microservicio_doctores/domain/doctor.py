class Doctor:
    def __init__(self, id_doctor: int, nombre: str, especialidad: str):
        self.id_doctor = id_doctor
        self.nombre = nombre
        self.especialidad = especialidad

    def __repr__(self):
        return f"Doctor(id={self.id_doctor}, nombre={self.nombre}, especialidad={self.especialidad})"
