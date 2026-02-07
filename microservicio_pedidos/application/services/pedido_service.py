from typing import Optional
from microservicio_pedidos.domain.pedido import Pedido
from microservicio_pedidos.application.ports.pedido_repository import PedidoRepositoryPort

class PedidoService:
    def __init__(self, repository: PedidoRepositoryPort):
        self.repository = repository

    def crear_pedido(self, items: str, total: float) -> Pedido:
        # Por defecto estado PENDIENTE
        nuevo_pedido = Pedido(id_pedido=None, items=items, total=total, estado="PENDIENTE")
        return self.repository.save(nuevo_pedido)

    def obtener_pedido(self, id_pedido: int) -> Optional[Pedido]:
        return self.repository.find_by_id(id_pedido)

    def actualizar_pedido(self, id_pedido: int, estado: str) -> Optional[Pedido]:
        pedido = self.repository.find_by_id(id_pedido)
        if not pedido:
            return None
        pedido.estado = estado
        return self.repository.update(pedido)

    def cancelar_pedido(self, id_pedido: int) -> bool:
        return self.repository.delete(id_pedido)
