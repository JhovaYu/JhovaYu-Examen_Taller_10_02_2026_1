from typing import List, Optional
from microservicio_doctores.domain.doctor import Doctor
from microservicio_doctores.application.ports.doctor_repository import DoctorRepositoryPort

class DoctorService:
    def __init__(self, repository: DoctorRepositoryPort):
        self.repository = repository

    def registrar_doctor(self, nombre: str, especialidad: str) -> Doctor:
        doctor = Doctor(id_doctor=0, nombre=nombre, especialidad=especialidad)
        return self.repository.save(doctor)

    def consultar_doctor(self, id_doctor: int) -> Optional[Doctor]:
        return self.repository.find_by_id(id_doctor)

    def listar_doctores(self) -> List[Doctor]:
        return self.repository.find_all()

    def eliminar_doctor(self, id_doctor: int) -> bool:
        return self.repository.delete(id_doctor)

    def actualizar_doctor(self, id_doctor: int, nombre: str, especialidad: str) -> Optional[Doctor]:
        return self.repository.update(id_doctor, nombre, especialidad)
