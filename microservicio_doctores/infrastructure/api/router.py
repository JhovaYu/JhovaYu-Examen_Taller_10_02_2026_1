from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from microservicio_doctores.application.services.doctor_service import DoctorService
from microservicio_doctores.infrastructure.adapters.sqlite_repository import SqliteDoctorRepository

router = APIRouter()

# Inyección de dependencias manual
repository = SqliteDoctorRepository()
service = DoctorService(repository)

class DoctorCreate(BaseModel):
    nombre: str
    especialidad: str

class DoctorResponse(BaseModel):
    id_doctor: int
    nombre: str
    especialidad: str

@router.post("/doctores/", response_model=DoctorResponse)
def registrar_doctor(doctor: DoctorCreate):
    try:
        nuevo_doctor = service.registrar_doctor(doctor.nombre, doctor.especialidad)
        return DoctorResponse(id_doctor=nuevo_doctor.id_doctor, nombre=nuevo_doctor.nombre, especialidad=nuevo_doctor.especialidad)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/doctores/{id_doctor}", response_model=DoctorResponse)
def consultar_doctor(id_doctor: int):
    doctor = service.consultar_doctor(id_doctor)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return DoctorResponse(id_doctor=doctor.id_doctor, nombre=doctor.nombre, especialidad=doctor.especialidad)

@router.get("/doctores/", response_model=List[DoctorResponse])
def listar_doctores():
    doctores = service.listar_doctores()
    return [DoctorResponse(id_doctor=d.id_doctor, nombre=d.nombre, especialidad=d.especialidad) for d in doctores]
