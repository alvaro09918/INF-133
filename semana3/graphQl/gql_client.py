import requests

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'



# Definir la consulta GraphQL con parametros de ID
query = """
    {
        estudiantePorId(id: 2){
            nombre
            apellido
        }
    }
"""

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)

# Definir la consulta GraphQL con parametros de NOMBRE Y APELLIDO
query = """
    {
        estudiantePorNombreApellido(nombre:"Jose", apellido:"Lopez"){
            id
            nombre 
            apellido
            carrera
        }
    }
"""

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)

# Definir la consulta GraphQL con parametros de CARRERA 
query = """
    {
        estudiantePorCarrera(carrera:"Arquitectura"){
            nombre 
            apellido
            carrera
        }
    }
"""

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)

# Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

# Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
mutation {
        crearEstudiante(nombre: "Ivan", apellido: "Gomez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

# Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
mutation {
        crearEstudiante(nombre: "Luisa", apellido: "ramirez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)
# Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
mutation {
        crearEstudiante(nombre: "Liz", apellido: "Leny", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

# Definir la consulta GraphQL

query = """
    {
        estudiantes{
            id
            nombre 
            apellido
            carrera
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)

# Definir la consulta GraphQL con parametros de CARRERA Lista de estudiantes con la carrera de Arquitectura
query = """
    {
        estudiantesPorCarrera(carrera:"Arquitectura"){
            nombre 
            apellido
            carrera
        }
    }
"""

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)

# Definir la consulta GraphQL para eliminar un estudiante
query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)

