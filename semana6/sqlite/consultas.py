# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("institutos.db") #estamos tomando la bd de mi_primera_db2, no de la primera xq no es persistente Y NO CORRE SI NO SE EJECUTA PRIMERO EL OTRO ARCHIVO


# Insertamos nuevos estudiantes y carreras
conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Licenciatura en Contabilidad', 4)
    """
)

conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre, apellido, fecha_nacimiento) 
    VALUES ('Carlos', 'Gomez', '2001-02-10')
    """
)
# Consultar datos
print("CARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)

# Consultar datos
print("\nESTUDIANTES:")
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)

#consultar datos de matriculacion INNER JOIN
print("\nMATRICULAS:INNER JOIN")
cursor=conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULAS.fecha
    FROM MATRICULAS
    JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id
    JOIN CARRERAS ON MATRICULAS.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)


#consultar datos de matriculacion left JOIN
print("\nMATRICULAS:LEFT JOIN")
cursor=conn.execute(
    """
    SELECT CARRERAS.nombre, ESTUDIANTES.nombre
    FROM CARRERAS
    LEFT JOIN MATRICULAS ON CARRERAS.id = MATRICULAS.carrera_id
    LEFT JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id;
    """
)  
for row in cursor:
    print(row)

#consultar datos de matriculacion RIGHT JOIN
print("\nMATRICULAS:RIGHT JOIN")
cursor=conn.execute(
    """
    SELECT ESTUDIANTES.nombre, CARRERAS.nombre
    FROM ESTUDIANTES
    LEFT JOIN MATRICULAS ON ESTUDIANTES.id = MATRICULAS.estudiante_id
    LEFT JOIN CARRERAS ON MATRICULAS.carrera_id = CARRERAS.id;
    """
)  
for row in cursor:
    print(row) 
    
#confirmar commit
conn.commit()
#cerrar conexion
conn.close()