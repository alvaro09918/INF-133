from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field, Mutation


class Estudiante(ObjectType):
    id = Int()
    nombre = String()
    apellido = String()
    carrera = String()
    
estudiantes = [
    Estudiante(
        id=1, nombre="Pedrito", apellido="García", carrera="Ingeniería de Sistemas"
    ),
    Estudiante(
        id=2, nombre="Jose", apellido="Lopez", carrera="Arquitectura"
    ),
    
]

class Query(ObjectType):
    estudiantes = List(Estudiante)
    estudiante_por_id=Field(Estudiante, id=Int())
    estudiante_por_nombre_apellido=Field(Estudiante,nombre=String(), apellido=String())
    estudiante_por_carrera=Field(Estudiante, carrera=String())
    estudiantes_por_carrera=List(Estudiante, carrera=String())

    def resolve_estudiantes(root, info):
        return estudiantes
    
    def resolve_estudiante_por_id(root, info, id):
        for estudiante in estudiantes:
            if estudiante.id == id:
                return estudiante
        return None
    
    def resolve_estudiante_por_nombre_apellido(root, info, nombre, apellido):
        for estudiante in estudiantes:
            if estudiante.nombre==nombre and estudiante.apellido==apellido:
                return estudiante
        return None
    
    def resolve_estudiante_por_carrera(root, info, carrera):
        for estudiante in estudiantes:
            if estudiante.carrera==carrera:
                return estudiante
        return None
    
    # muestra la lista de los estudiantes con la misma carrera
    def resolve_estudiantes_por_carrera(root, info, carrera):
        estudiante_carrera=[]
        for estudiante in estudiantes:
            if estudiante.carrera==carrera:
                estudiante_carrera.append(estudiante)
        return estudiante_carrera
    

class CrearEstudiante(Mutation):
    class Arguments:
        nombre = String()
        apellido = String()
        carrera = String()

    estudiante = Field(Estudiante)

    def mutate(root, info, nombre, apellido, carrera):
        nuevo_estudiante = Estudiante(
            id=len(estudiantes) + 1, 
            nombre=nombre, 
            apellido=apellido, 
            carrera=carrera
        )
        estudiantes.append(nuevo_estudiante)

        return CrearEstudiante(estudiante=nuevo_estudiante)


class DeleteEstudiante(Mutation):
    class Arguments:
        id = Int()

    estudiante = Field(Estudiante)

    def mutate(root, info, id):
        for i, estudiante in enumerate(estudiantes):
            if estudiante.id == id:
                estudiantes.pop(i)
                return DeleteEstudiante(estudiante=estudiante)
        return None
    
#modificar estudiante por ID
class ActualizarEstudiante(Mutation):
    class Arguments:
        id = Int()
        nombre = String()
        apellido = String()
        carrera = String()

    estudiante = Field(Estudiante)

    def mutate(root, info, id, nombre, apellido, carrera):
        for estudiante in estudiantes:
            if estudiante.id == id:
                estudiante.nombre = nombre
                estudiante.apellido = apellido
                estudiante.carrera = carrera
                return ActualizarEstudiante(estudiante=estudiante)
        return None

class actualizarCarrera(Mutation):
    class Arguments:
        nombre = String()
        
        carrera = String()

    estudiante = Field(Estudiante)

    def mutate(root, info, nombre, carrera):
        for estudiante in estudiantes:
            if estudiante.nombre == nombre:
                estudiante.carrera = carrera
                return actualizarCarrera(estudiante=estudiante)
        return None
    

    
#elimina los estudiantes de una determinada carrera
class DeleteCarrera(Mutation):
    class Arguments:
        carrera=String()

    estudiante = Field(Estudiante)

    def mutate(root, info, carrera):
        estudiantes_eliminados=[]
        i=0
        while(i<len(estudiantes)):
            if(estudiantes[i].carrera==carrera):
                estudiantes_eliminados.append(estudiantes.pop(i))
            else:
                i+=1
        return DeleteCarrera(estudiantes=estudiantes_eliminados)  
    
class Mutations(ObjectType):
    crear_estudiante = CrearEstudiante.Field()
    delete_estudiante = DeleteEstudiante.Field()
    actualizar_estudiante=ActualizarEstudiante.Field()
    actualizar_carrera=actualizarCarrera.Field()
    delete_carrera=DeleteCarrera.Field()

schema = Schema(query=Query, mutation=Mutations)


class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()