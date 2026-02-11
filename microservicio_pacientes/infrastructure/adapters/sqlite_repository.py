import sqlite3
from typing import List, Optional
from microservicio_pacientes.domain.paciente import Paciente
from microservicio_pacientes.application.ports.paciente_repository import PacienteRepositoryPort

class SqlitePacienteRepository(PacienteRepositoryPort):
    def __init__(self, db_path: str = "pacientes.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()
        conn.close()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def save(self, paciente: Paciente) -> Paciente:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pacientes (nombre, email) VALUES (?, ?)", (paciente.nombre, paciente.email))
        paciente.id_paciente = cursor.lastrowid
        conn.commit()
        conn.close()
        return paciente

    def find_by_id(self, id_paciente: int) -> Optional[Paciente]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email FROM pacientes WHERE id = ?", (id_paciente,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Paciente(id_paciente=row[0], nombre=row[1], email=row[2])
        return None

    def find_all(self) -> List[Paciente]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email FROM pacientes")
        rows = cursor.fetchall()
        conn.close()
        return [Paciente(id_paciente=row[0], nombre=row[1], email=row[2]) for row in rows]

    def delete(self, id_paciente: int) -> bool:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pacientes WHERE id = ?", (id_paciente,))
        changes = cursor.rowcount
        conn.commit()
        conn.close()
        return changes > 0
