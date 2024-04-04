import sqlite3
conn =  sqlite3.connect("instituto.db")

conn.execute(
    """INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento)
    VALUES ('carlos', 'gomez', '2001-02-10')
    """
)
conn.execute(
    """INSERT INTO CARRERAS (nombre, duracion)
    VALUES ('licenciatura en contabilidad', 4)
    """
)

conn.execute(
    """SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha
    FROM MATRICULACION 
    JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id
    JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
    """
)
conn.commit()
conn.close()