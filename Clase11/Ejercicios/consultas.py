import sqlite3
conn = sqlite3.connect("personal.db")

conn.execute(
    """INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
    VALUES ('Ventas', '2020-04-10')"""
)
conn.execute(
    """INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
    VALUES ('Marketing', '2020-04-11')"""
)

conn.execute(
    """INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES ('Gerente de ventas', 'senior', '2020-04-10')"""
)
conn.execute(
    """INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES ('Analista de Marketing', 'junior', '2020-04-11')"""
)
conn.execute(
    """INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES ('Representante de Ventas', 'junior', '2020-04-12')"""
)

conn.execute(
    """INSERT INTO EMPLEADOS (nombres, apellido_materno, apellido_paterno, fecha_contratacion, departamento_id, cargo_id)
    VALUES ('Juan', 'Gonzales', 'Perez', '2023-05-15', 1, 1)"""
)
conn.execute(
    """INSERT INTO EMPLEADOS (nombres, apellido_materno, apellido_paterno, fecha_contratacion, departamento_id, cargo_id)
    VALUES ('Maria', 'Lopez', 'Martines', '2023-06-20', 2, 2)"""
)
conn.execute(
    """INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin)
    VALUES (1, 3000, '2024-04-01', '2025-04-30' )"""
)
conn.execute(
    """INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin)
    VALUES (2, 3500, '2023-07-01', '2024-04-30' )"""
)

conn.commit()