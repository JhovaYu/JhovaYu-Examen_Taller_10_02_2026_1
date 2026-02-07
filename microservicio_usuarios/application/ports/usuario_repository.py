from abc import ABC, abstractmethod
from typing import Optional, List
from microservicio_usuarios.domain.usuario import Usuario

class UsuarioRepositoryPort(ABC):
    @abstractmethod
    def save(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def find_by_id(self, id_usuario: int) -> Optional[Usuario]:
        pass

    @abstractmethod
    def find_all(self) -> List[Usuario]:
        pass

    @abstractmethod
    def update(self, usuario: Usuario) -> Optional[Usuario]:
        pass

    @abstractmethod
    def delete(self, id_usuario: int) -> bool:
        pass
