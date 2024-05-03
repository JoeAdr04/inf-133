import sqlite3 # importar el modulo sqllite3

conn =  sqlite3.connect("instituto.db") #crea la conexion a la base de datos

#crear tablas de carrera


try :
    conn.execute(
        """
        CREATE TABLE CARRERAS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        duracion INTEGER NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla CARRERAS ya existe")

conn.execute(
    """
    INSERT INTO CARRERAS (nombre,duracion)
    VALUES ('Licenciatura en administracion',4)
    """
)

#consultar datos
print ("CARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)

try:
    conn.execute(
        """
        CREATE TABLE ESTUDIANTES
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        fecha_nacimiento DATE NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla ESTUDIANTES ya existe")

conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento)
    VALUES ('pedrito', 'choque', '2000-05-12')
    """
)
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento)
    VALUES ('maria', 'tapia', '1999-10-22')
    """
)

print ("estidiantes") #consulta datos de estuiantes
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)

try:
    conn.execute(
        """
        CREATE TABLE MATRICULACION
        (id INTEGER PRIMARY KEY,
        estudiante_id INTEGER NOT NULL,
        carrera_id INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
        FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla MATRICULAS ya existe")

conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
    VALUES (1, 1, '2024-01-15')
    """
)
conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
    VALUES (2, 2, '2024-01-20')
    """
)
conn.execute(
    """
    INSERT INTO MATRICULACION (estudiante_id, carrera_id, fecha)
    VALUES (1, 2, '2024-01-25')
    """
)

#consultar datos de matriculacion

print("\nMatriculacion:")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES .nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha
    FROM MATRICULACION 
    JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id
    JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)




#listar
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
    )

for row in cursor:
    print(row)

#actualixar la fila de una tabla de de matriculacion
conn.execute(
    """
    UPDATE MATRICULACION
    SET fecha = '2024-01-30'
    WHERE id = 2  
    """
)
#listar
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
    )

for row in cursor:
    print(row)

#borrar una matriculacion
conn.execute(
    """
    DELETE FROM MATRICULACION 
    WHERE id = 1
    """
)

#listar
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
    )

for row in cursor:
    print(row)

conn.commit()

conn.close()