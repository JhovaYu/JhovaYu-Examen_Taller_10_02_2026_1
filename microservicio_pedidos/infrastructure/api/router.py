from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from microservicio_pedidos.application.services.pedido_service import PedidoService
from microservicio_pedidos.infrastructure.adapters.sqlite_repository import SqlitePedidoRepository

class PedidoCreateDTO(BaseModel):
    items: str
    total: float

class PedidoUpdateDTO(BaseModel):
    estado: str

class PedidoResponseDTO(BaseModel):
    id_pedido: int
    items: str
    total: float
    estado: str

def get_service():
    repository = SqlitePedidoRepository()
    return PedidoService(repository)

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@router.post("/", response_model=PedidoResponseDTO, status_code=201)
def create_pedido(pedido_dto: PedidoCreateDTO, service: PedidoService = Depends(get_service)):
    pedido = service.crear_pedido(pedido_dto.items, pedido_dto.total)
    return PedidoResponseDTO(
        id_pedido=pedido.id_pedido,
        items=pedido.items,
        total=pedido.total,
        estado=pedido.estado
    )

@router.get("/{id_pedido}", response_model=PedidoResponseDTO)
def get_pedido(id_pedido: int, service: PedidoService = Depends(get_service)):
    pedido = service.obtener_pedido(id_pedido)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return PedidoResponseDTO(
        id_pedido=pedido.id_pedido,
        items=pedido.items,
        total=pedido.total,
        estado=pedido.estado
    )

@router.put("/{id_pedido}", response_model=PedidoResponseDTO)
def update_pedido(id_pedido: int, pedido_dto: PedidoUpdateDTO, service: PedidoService = Depends(get_service)):
    pedido = service.actualizar_pedido(id_pedido, pedido_dto.estado)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return PedidoResponseDTO(
        id_pedido=pedido.id_pedido,
        items=pedido.items,
        total=pedido.total,
        estado=pedido.estado
    )

@router.delete("/{id_pedido}", status_code=204)
def delete_pedido(id_pedido: int, service: PedidoService = Depends(get_service)):
    if not service.cancelar_pedido(id_pedido):
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
