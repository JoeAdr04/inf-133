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

print("\nMATRICULAS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULAS.fecha 
    FROM MATRICULAS
    JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULAS.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)

print("\nMATRICULAS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT CARRERAS.nombre, ESTUDIANTES.nombre
    FROM CARRERAS
    LEFT JOIN MATRICULAS ON CARRERAS.id = MATRICULAS.carrera_id
    LEFT JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id;
    """
)
for row in cursor:
    print(row)
conn.commit()
conn.close()