from abc import ABC, abstractmethod
from typing import Optional, List
from microservicio_pacientes.domain.paciente import Paciente

class PacienteRepositoryPort(ABC):
    @abstractmethod
    def save(self, paciente: Paciente) -> Paciente:
        pass

    @abstractmethod
    def find_by_id(self, id_paciente: int) -> Optional[Paciente]:
        pass

    @abstractmethod
    def find_all(self) -> List[Paciente]:
        pass

    @abstractmethod
    def delete(self, id_paciente: int) -> bool:
        pass
