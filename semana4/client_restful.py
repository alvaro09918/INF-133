import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"

# POST agrega un nuevo estudiante por la ruta /estudiantes

ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)