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
