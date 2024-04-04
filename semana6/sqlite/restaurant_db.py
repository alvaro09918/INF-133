import sqlite3
conn = sqlite3.connect("restaurant.db")


# Crear tabla de PLATOS
try :
    conn.execute(
        """
        CREATE TABLE PLATOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio INTEGER NOT NULL,
        categoria TEXT NOT NULL);
        
        """
    )
except sqlite3.OperationalError:
    print("La tabla PLATOS ya existe")
    
# Insertar datos de PLATOS
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Pizza',10.99,'Italiana') 
    """
    
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Hamburguesa',8.99,'Americana') 
    """
    
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Sushi',12.99,'Japonesa') 
    """
    
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Ensalada',6.99,'Vegetariana') 
    """
    
)
# Consultar datos
print("PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
    
#CREAR MESAS   
try :
    conn.execute(
        """
        CREATE TABLE MESAS
        (id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL);
        
        """
    )
except sqlite3.OperationalError:
    print("La tabla MESAS ya existe")   

# Insertar datos de mesas
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
# Consultar mesas
print("\nMESAS:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)

#CREAR PEDIDOS
try :
    conn.execute(
        """
        CREATE TABLE PEDIDOS
        (id INTEGER PRIMARY KEY,
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha DATE NOT NULL,
        
        FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
        FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
    
        
        """
    )
except sqlite3.OperationalError:
    print("La tabla PEDIDOS ya existe")      

#Insertar datos de PEDIDOS
conn.execute(
    
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (1, 2, 2, '2024-04-01')
    """
) 
conn.execute(
    
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (2, 3, 1, '2024-04-01')
    """
)  
conn.execute(
    
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (3, 1, 3, '2024-04-01')
    """
)  
conn.execute(
    
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha)
    VALUES (4, 4, 1, '2024-04-01')
    """
)     

# LISTAR PEDIDOS
print("\nPEDIDOS:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)

#=========================ACTUALIZAR PLATO POR ID=====================================
#actualizar precio
conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)

# Consultar datos
print("\nACTUALIZAR PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
#actualizar categoria
conn.execute(
    """
    UPDATE PLATOS
    SET categoria ='Fusion'
    WHERE id = 3
    """
)

# Consultar datos
print("\nACTUALIZAR PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
 
#=========================ELIMINAR POR ID=====================================   
#ELIMINAR PLATO POR ID
conn.execute(
    """
    DELETE FROM PLATOS
    WHERE id=4
    
    """
) 
# Consultar datos
print("\nELIMINAR PLATOS:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
#ELIMINAR PEDIDOS POR ID
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id=3
    
    """
) 
# Consultar datos
print("\nELIMINAR PEDIDOS:")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)   
    
    
    
        
# Confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()