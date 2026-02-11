import uvicorn
from fastapi import FastAPI
from microservicio_pacientes.infrastructure.api.router import router

app = FastAPI(title="Microservicio de Pacientes", version="1.0.0", description="API Hexagonal para gestión de pacientes")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("microservicio_pacientes.main:app", host="127.0.0.1", port=8001, reload=True)
