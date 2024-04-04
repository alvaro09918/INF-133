# Importar módulo sqlite3
import sqlite3
# Crear conexión a la base de datos
conn = sqlite3.connect("institutos.db")

# Crear tabla de carreras
conn.execute(
    """
    CREATE TABLE CARRERAS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL);
    """
)


# Insertar datos de carreras
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Ingeniería en Informática', 5) 
    """
    #en value se ponen los datos de nombre y duracion
)

conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Licenciatura en Administración', 4)
    """
)

# Consultar datos
print("CARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS") #select selecciona * todo from palabra reservada 
for row in cursor:
    print(row) # va imprimir tuplas

# Crear tablas de estudiantes
conn.execute(
    """
    CREATE TABLE ESTUDIANTES
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL);
    """
)

#insertar datos de estudiantes
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('Juan', 'Perez', '2000-05-15')
    """
    #para poner cadenas entre comillas simples 
)
conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('María', 'Lopez', '1999-08-20')
    """
)

# Consultar datos de estudiantes
print("\nESTUDIANTES:")
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)

# Crear tabla de matriculación
conn.execute(
    """
    CREATE TABLE MATRICULAS
    (id INTEGER PRIMARY KEY,
    estudiante_id INTEGER NOT NULL,
    carrera_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
    FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
    """
    #las llaves foraneas se sercioran de que no entre datos q no existe creo, las ultimas dos lineas comprueban eso
)
# Insertar datos de matriculación
conn.execute(
    """
    INSERT INTO MATRICULAS (estudiante_id, carrera_id, fecha) 
    VALUES (1, 1, '2024-01-15')
    """
)
conn.execute(
    """
    INSERT INTO MATRICULAS (estudiante_id, carrera_id, fecha) 
    VALUES (2, 2, '2024-01-20')
    """
)

conn.execute(
    """
    INSERT INTO MATRICULAS (estudiante_id, carrera_id, fecha)
    VALUES (1, 2, '2024-01-25')
    """
)
# Consultar datos de matriculación
print("\nMATRICULACION:")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULAS.fecha 
    FROM MATRICULAS
    JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULAS.carrera_id = CARRERAS.id
    """
    #join es unir 
)
for row in cursor:
    print(row)

#listar datos de matriculacion
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULAS"
)
for row in cursor:
    print(row)

# Actualizar una fila de la tabla de matriculación
conn.execute(
    """
    UPDATE MATRICULAS
    SET fecha = '2024-01-30'
    WHERE id = 2
    """
)

print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULAS"
)
for row in cursor:
    print(row)
    
# Eliminar una fila de la tabla de matriculación
conn.execute(
    """
    DELETE FROM MATRICULAS
    WHERE id = 1
    """
)
print("\nMATRICULACION:")
cursor = conn.execute(
    "SELECT * FROM MATRICULAS"
)
for row in cursor:
    print(row)

#confirmar commit
conn.commit()
#cerrar conexion
conn.close()
    

