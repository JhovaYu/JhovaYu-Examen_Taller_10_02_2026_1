import sqlite3
from typing import List, Optional
from microservicio_pedidos.domain.pedido import Pedido
from microservicio_pedidos.application.ports.pedido_repository import PedidoRepositoryPort

class SqlitePedidoRepository(PedidoRepositoryPort):
    def __init__(self, db_path: str = "pedidos.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                items TEXT NOT NULL,
                total REAL NOT NULL,
                estado TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def save(self, pedido: Pedido) -> Pedido:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pedidos (items, total, estado) VALUES (?, ?, ?)", 
                       (pedido.items, pedido.total, pedido.estado))
        pedido.id_pedido = cursor.lastrowid
        conn.commit()
        conn.close()
        return pedido

    def find_by_id(self, id_pedido: int) -> Optional[Pedido]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, items, total, estado FROM pedidos WHERE id = ?", (id_pedido,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Pedido(id_pedido=row[0], items=row[1], total=row[2], estado=row[3])
        return None

    def update(self, pedido: Pedido) -> Optional[Pedido]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE pedidos SET estado = ? WHERE id = ?", (pedido.estado, pedido.id_pedido))
        conn.commit()
        conn.close()
        return pedido

    def delete(self, id_pedido: int) -> bool:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pedidos WHERE id = ?", (id_pedido,))
        changes = conn.total_changes
        conn.commit()
        conn.close()
        return changes > 0
