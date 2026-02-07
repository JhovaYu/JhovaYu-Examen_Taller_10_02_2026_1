from typing import List, Optional
from microservicio_usuarios.domain.usuario import Usuario
from microservicio_usuarios.application.ports.usuario_repository import UsuarioRepositoryPort

class UsuarioService:
    def __init__(self, repository: UsuarioRepositoryPort):
        self.repository = repository

    def registrar_usuario(self, nombre: str, email: str) -> Usuario:
        # Aquí podría ir lógica de negocio, ej: validar email único (si el repo lo soportara)
        # Por ahora creamos un ID temporal o dejamos que el repo lo maneje. 
        # Para simplificar este ejemplo sin DB real autoincremental compleja, asumiremos que el repo maneja el ID.
        nuevo_usuario = Usuario(id_usuario=None, nombre=nombre, email=email)
        return self.repository.save(nuevo_usuario)

    def obtener_usuario(self, id_usuario: int) -> Optional[Usuario]:
        return self.repository.find_by_id(id_usuario)

    def listar_usuarios(self) -> List[Usuario]:
        return self.repository.find_all()

    def modificar_usuario(self, id_usuario: int, nombre: str, email: str) -> Optional[Usuario]:
        usuario_existente = self.repository.find_by_id(id_usuario)
        if not usuario_existente:
            return None
        
        usuario_existente.nombre = nombre
        usuario_existente.email = email
        return self.repository.update(usuario_existente)

    def eliminar_usuario(self, id_usuario: int) -> bool:
        return self.repository.delete(id_usuario)
