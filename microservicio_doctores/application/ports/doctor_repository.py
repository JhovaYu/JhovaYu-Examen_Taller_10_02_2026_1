from abc import ABC, abstractmethod
from typing import Optional, List
from microservicio_doctores.domain.doctor import Doctor

class DoctorRepositoryPort(ABC):
    @abstractmethod
    def save(self, doctor: Doctor) -> Doctor:
        pass

    @abstractmethod
    def find_by_id(self, id_doctor: int) -> Optional[Doctor]:
        pass

    @abstractmethod
    def find_all(self) -> List[Doctor]:
        pass

    @abstractmethod
    def delete(self, id_doctor: int) -> bool:
        pass

    @abstractmethod
    def update(self, id_doctor: int, nombre: str, especialidad: str) -> Optional[Doctor]:
        pass
