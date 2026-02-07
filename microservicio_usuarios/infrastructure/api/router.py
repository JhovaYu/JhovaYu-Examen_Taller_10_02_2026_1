from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from typing import List
from microservicio_usuarios.application.services.usuario_service import UsuarioService
from microservicio_usuarios.infrastructure.adapters.sqlite_repository import SqliteUsuarioRepository

# DTOs (Data Transfer Objects)
class UsuarioCreateDTO(BaseModel):
    nombre: str
    email: EmailStr

class UsuarioResponseDTO(BaseModel):
    id_usuario: int
    nombre: str
    email: EmailStr

# Factory para inyección de dependencias
def get_service():
    repository = SqliteUsuarioRepository()
    return UsuarioService(repository)

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/", response_model=UsuarioResponseDTO, status_code=201)
def create_usuario(usuario_dto: UsuarioCreateDTO, service: UsuarioService = Depends(get_service)):
    try:
        usuario_creado = service.registrar_usuario(usuario_dto.nombre, usuario_dto.email)
        return UsuarioResponseDTO(
            id_usuario=usuario_creado.id_usuario,
            nombre=usuario_creado.nombre,
            email=usuario_creado.email
        )
    except Exception as e:
        error_msg = str(e)
        if "UNIQUE constraint failed" in error_msg:
            raise HTTPException(status_code=400, detail="El email ya está registrado. Intenta con otro.")
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{id_usuario}", response_model=UsuarioResponseDTO)
def get_usuario(id_usuario: int, service: UsuarioService = Depends(get_service)):
    usuario = service.obtener_usuario(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UsuarioResponseDTO(
        id_usuario=usuario.id_usuario,
        nombre=usuario.nombre,
        email=usuario.email
    )

@router.put("/{id_usuario}", response_model=UsuarioResponseDTO)
def update_usuario(id_usuario: int, usuario_dto: UsuarioCreateDTO, service: UsuarioService = Depends(get_service)):
    usuario = service.modificar_usuario(id_usuario, usuario_dto.nombre, usuario_dto.email)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UsuarioResponseDTO(
        id_usuario=usuario.id_usuario,
        nombre=usuario.nombre,
        email=usuario.email
    )

@router.delete("/{id_usuario}", status_code=204)
def delete_usuario(id_usuario: int, service: UsuarioService = Depends(get_service)):
    if not service.eliminar_usuario(id_usuario):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
