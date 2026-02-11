from typing import List, Optional
from microservicio_pacientes.domain.paciente import Paciente
from microservicio_pacientes.application.ports.paciente_repository import PacienteRepositoryPort

class PacienteService:
    def __init__(self, repository: PacienteRepositoryPort):
        self.repository = repository

    def registrar_paciente(self, nombre: str, email: str) -> Paciente:
        paciente = Paciente(id_paciente=0, nombre=nombre, email=email)
        return self.repository.save(paciente)

    def consultar_paciente(self, id_paciente: int) -> Optional[Paciente]:
        return self.repository.find_by_id(id_paciente)

    def listar_pacientes(self) -> List[Paciente]:
        return self.repository.find_all()

    def eliminar_paciente(self, id_paciente: int) -> bool:
        return self.repository.delete(id_paciente)
    
    def eliminar_paciente(self, id_paciente: int) -> bool:
        return self.repository.delete(id_paciente)  

    

    