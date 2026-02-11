import sys
import os

project_root = r"c:\Users\alfom\Documents\Proyectos_Programacion\taller4\examen_taller\Microservicios_Usuarios"
sys.path.append(project_root)

try:
    print("Checking Pacientes DELETE...")
    from microservicio_pacientes.infrastructure.api.router import eliminar_paciente
    from microservicio_pacientes.application.services.paciente_service import PacienteService
    if not hasattr(PacienteService, 'eliminar_paciente'):
        raise Exception("PacienteService.eliminar_paciente missing")
    print("Pacientes DELETE OK.")

    print("Checking Doctores PUT...")
    from microservicio_doctores.infrastructure.api.router import actualizar_doctor
    from microservicio_doctores.application.services.doctor_service import DoctorService
    if not hasattr(DoctorService, 'actualizar_doctor'):
        raise Exception("DoctorService.actualizar_doctor missing")
    print("Doctores PUT OK.")

    print("All checks passed.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
