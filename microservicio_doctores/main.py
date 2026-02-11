import uvicorn
from fastapi import FastAPI
from microservicio_doctores.infrastructure.api.router import router

app = FastAPI(title="Microservicio de Doctores", version="1.0.0", description="API Hexagonal para gestión de doctores")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("microservicio_doctores.main:app", host="127.0.0.1", port=8002, reload=True)
