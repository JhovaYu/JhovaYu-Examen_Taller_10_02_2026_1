from typing import List

class Pedido:
    def __init__(self, id_pedido: int, items: str, total: float, estado: str):
        # Items simplificado a string para este ejemplo, podría ser una lista de obj
        self.id_pedido = id_pedido
        self.items = items 
        self.total = total
        self.estado = estado

    def __repr__(self):
        return f"Pedido(id={self.id_pedido}, items={self.items}, total={self.total}, estado={self.estado})"
