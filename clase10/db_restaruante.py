import sqlite3
conn = sqlite3.connect("restaurante.db")

try:  
    conn.execute(
        """
        CREATE TABLE PLATOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL );
        """
    )
except sqlite3.OperationalError:
    print("la tabla de paltos ya existe")

conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('pizzA', 10.99, 'italiana')
    """
)

conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('hamburguesa', 8.99, 'americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('sushi', 12.99, 'japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('ensalada', 6.99, 'vegetariana')
    """
)
try:
    conn.execute(
        """
        CREATE TABLE MESAS
        (id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("la tabla de mesas ya existe")

conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (2)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (4)
    """
)

try:
    conn.execute(
        """
        CREATE TABLE PEDIDOS
        (id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha DATE NOT NULL,
        FOREIGN KEY (PLATO_ID) REFERENCES PLATOS(id),
        FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
        """
    )
except sqlite3.OperationalError:
    print("la tabla de pedidos ya existe")

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad,fecha)
    VALUES (1, 2, 2, 2024-04-01)
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad,fecha)
    VALUES (2, 3, 1, 2024-04-01)
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad,fecha)
    VALUES (3, 1, 3, 2024-04-02)
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad,fecha)
    VALUES (4, 4, 1, 2024-04-02)
    """
)

print ("PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
print ("MESAS:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 3
    """
)
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'fusion'
    WHERE id = 3
    """
)

conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 3
    """
)
print("\PEDIDOS:")


for row in cursor:
    print(row)

cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.nombre, PEDIDOS.cantidad, PEDIDOS.fecha
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESA ON PEDIDOS.mesa_id = MESAS.id
    """
)

for row in cursor:
    print(row)

cursor = conn.execute(
    """
    SELECT PEDIDOS.nombre,PEDIDOS.cantidad, PEDIDOS,fecha, PLATOS.nombre, PALTOS.precio, PLATOS.categoria
    FROM PEDIDOS
    LEFT JOIN PEDIDOS ON PLATOS.id = PEDIDOS.plato_id
    LEFT JOIN PLATOS ON PEDDIOS. = ESTUDIANTES.id;
    """
)
for row in cursor:
    print(row)

conn.commit()
conn.close()