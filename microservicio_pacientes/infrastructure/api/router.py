from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from microservicio_pacientes.application.services.paciente_service import PacienteService
from microservicio_pacientes.infrastructure.adapters.sqlite_repository import SqlitePacienteRepository

router = APIRouter()

# Inyección de dependencias manual
repository = SqlitePacienteRepository()
service = PacienteService(repository)

class PacienteCreate(BaseModel):
    nombre: str
    email: str

class PacienteResponse(BaseModel):
    id_paciente: int
    nombre: str
    email: str

@router.post("/pacientes/", response_model=PacienteResponse)
def registrar_paciente(paciente: PacienteCreate):
    try:
        nuevo_paciente = service.registrar_paciente(paciente.nombre, paciente.email)
        return PacienteResponse(id_paciente=nuevo_paciente.id_paciente, nombre=nuevo_paciente.nombre, email=nuevo_paciente.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/pacientes/{id_paciente}", response_model=PacienteResponse)
def consultar_paciente(id_paciente: int):
    paciente = service.consultar_paciente(id_paciente)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return PacienteResponse(id_paciente=paciente.id_paciente, nombre=paciente.nombre, email=paciente.email)

@router.get("/pacientes/", response_model=List[PacienteResponse])
def listar_pacientes():
    pacientes = service.listar_pacientes()
    return [PacienteResponse(id_paciente=p.id_paciente, nombre=p.nombre, email=p.email) for p in pacientes]

@router.delete("/pacientes/{id_paciente}")
def eliminar_paciente(id_paciente: int):
    eliminado = service.eliminar_paciente(id_paciente)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"message": "Paciente eliminado correctamente"}
