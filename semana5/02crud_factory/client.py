import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /chocolates
new_chocolate_data = {
    "chocolate_type": "bonbon",
    "peso": "10kg",
    "sabor": "fresa",
    "relleno": "coco",
    
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_vehicle_data = {
    "chocolate_type": "truffle",
    "peso": "12kg",
    "sabor": "menta",
    "relleno": "mani",
   
}
response = requests.post(url=url, json=new_vehicle_data, headers=headers)
print(response.json())

new_vehicle_data = {
    "chocolate_type": "tablet",
    "peso": "5kg",
    "sabor": "menta",
    "relleno": "mani",
   
}
response = requests.post(url=url, json=new_vehicle_data, headers=headers)
print(response.json())


# GET /chocolates
response = requests.get(url=url)
print(response.json())

# PUT /chocolates/{chocolates_id}
chocolate_id_to_update = 1
updated_chocolate_data = {
    "sabor": "limon"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("chocolate actualizado:", response.json())

# GET /chocolates
response = requests.get(url=url)
print(response.json())

# DELETE /chocolates/{chocolates_id}
chocolates_id_to_delete = 1
response = requests.delete(f"{url}/{chocolates_id_to_delete}")
print("chocolate eliminado:", response.json())

# GET /chocolate
response = requests.get(url=url)
print(response.json())