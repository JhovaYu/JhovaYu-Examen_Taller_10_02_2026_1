import sqlite3
from typing import List, Optional
from microservicio_doctores.domain.doctor import Doctor
from microservicio_doctores.application.ports.doctor_repository import DoctorRepositoryPort

class SqliteDoctorRepository(DoctorRepositoryPort):
    def __init__(self, db_path: str = "doctores.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS doctores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                especialidad TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def save(self, doctor: Doctor) -> Doctor:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO doctores (nombre, especialidad) VALUES (?, ?)", (doctor.nombre, doctor.especialidad))
        doctor.id_doctor = cursor.lastrowid
        conn.commit()
        conn.close()
        return doctor

    def find_by_id(self, id_doctor: int) -> Optional[Doctor]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, especialidad FROM doctores WHERE id = ?", (id_doctor,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Doctor(id_doctor=row[0], nombre=row[1], especialidad=row[2])
        return None

    def find_all(self) -> List[Doctor]:
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, especialidad FROM doctores")
        rows = cursor.fetchall()
        conn.close()
        return [Doctor(id_doctor=row[0], nombre=row[1], especialidad=row[2]) for row in rows]
