import sqlite3
from typing import List, Optional
from microservicio_usuarios.domain.usuario import Usuario
from microservicio_usuarios.application.ports.usuario_repository import UsuarioRepositoryPort

class SqliteUsuarioRepository(UsuarioRepositoryPort):
    def __init__(self, db_path: str = "usuarios.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()
        conn.close()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def save(self, usuario: Usuario) -> Usuario:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (usuario.nombre, usuario.email))
        usuario.id_usuario = cursor.lastrowid
        conn.commit()
        conn.close()
        return usuario

    def find_by_id(self, id_usuario: int) -> Optional[Usuario]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = ?", (id_usuario,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Usuario(id_usuario=row[0], nombre=row[1], email=row[2])
        return None

    def find_all(self) -> List[Usuario]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return [Usuario(id_usuario=row[0], nombre=row[1], email=row[2]) for row in rows]

    def update(self, usuario: Usuario) -> Optional[Usuario]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nombre = ?, email = ? WHERE id = ?", (usuario.nombre, usuario.email, usuario.id_usuario))
        conn.commit()
        conn.close()
        return usuario

    def delete(self, id_usuario: int) -> bool:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        changes = conn.total_changes
        conn.commit()
        conn.close()
        return changes > 0
