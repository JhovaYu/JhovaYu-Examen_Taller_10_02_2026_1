import uvicorn
from fastapi import FastAPI
from microservicio_pedidos.infrastructure.api.router import router

app = FastAPI(title="Microservicio de Pedidos", version="1.0.0", description="API Hexagonal para gestión de pedidos")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)
