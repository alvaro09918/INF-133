from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes=[
    {
        "id":1,
        "nombre":"Pedrito",
        "apellido":"Garcia",
        "carrera":"Ingenieria de Sistemas",
    },
]
class RESTRquestHandler(BaseHTTPRequestHandler):
    def do_GET( self):
        if self.path=='/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error":"Ruta no existente"}).encode('utf-8'))

    def do_POST(self):
        if self.path== '/agrega_estudiante':
            content_length=int(self.headers['Content-Length'])
            post_data=self.rfile.read(content_length)
            post_data=json.loads(post_data.decode('utf-8'))
            post_data['id']=len(estudiantes)+1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error":"Ruta no existente"}).encode('utf-8'))
    
def run_server(port=8000):
    try:
        server_address=('',port)
        httpd=HTTPServer(server_address,RESTRquestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

if __name__=="__main__":
    run_server()


