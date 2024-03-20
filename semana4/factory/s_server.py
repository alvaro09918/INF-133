from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class DeliveryVehicle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.packages_delivered = 0

    def deliver(self):
        if self.packages_delivered < self.capacity:
            self.packages_delivered += 1
            return "Entrega realizada con exito"
        else:
            return "El vehículo ha alcanzado su capacidad máxima de entregas"
        
class DeliveryService:
    @staticmethod
    def instace_vehicle(request_data):
        vehicle_type = request_data.get("vehicle_type")
        delivery_factory = DeliveryFactory()
        delivery_vehicle = delivery_factory.create_delivery_vehicle(vehicle_type)
        response_data = {"message": delivery_vehicle.deliver()}
        return response_data
    
class HTTPResponseHandler:
    @staticmethod
    def response_handler(handler,status,data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))
    
    @staticmethod
    def response_handler2(handler,status):
        handler.send_response(status)
        handler.end_headers()
        handler.wfile.write(b"Ruta no encontrada")

        
    



class Motorcycle(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=10)


class Drone(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=20)

class Scout(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=5)


class DeliveryFactory:
    def create_delivery_vehicle(self, vehicle_type):
        if vehicle_type == "motorcycle":
            return Motorcycle()
        elif vehicle_type == "drone":
            return Drone()
        elif vehicle_type == "scout":
            return Scout()
        else:
            raise ValueError("Tipo de vehículo de entrega no válido")


class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/delivery":
            data=self.read_data()
            vehicle_type =DeliveryService.instace_vehicle(data)
            HTTPResponseHandler.response_handler(self,200,vehicle_type)
        else:
            HTTPResponseHandler.response_handler2(self,404)
    
    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        request_data = json.loads(post_data.decode("utf-8"))
        return request_data



def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, DeliveryRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()