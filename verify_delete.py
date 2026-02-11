import sys
import os

project_root = r"c:\Users\alfom\Documents\Proyectos_Programacion\taller4\examen_taller\Microservicios_Usuarios"
sys.path.append(project_root)

try:
    from microservicio_doctores.infrastructure.api.router import eliminar_doctor
    print("Delete endpoint found.")
    from microservicio_doctores.application.services.doctor_service import DoctorService
    if hasattr(DoctorService, 'eliminar_doctor'):
        print("Service method found.")
    else:
        raise Exception("Service method missing")
    
    print("Syntax check passed.")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
