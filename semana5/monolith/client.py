

import requests
url = "http://localhost:8000"

#lista los posts
response = requests.get(f"{url}/posts")
print(response.text)

#busca y muestra un post por ID
response = requests.get(f"{url}/post/2")
print(response.text)

#crear un nuevo post pero no muestra todo el contenido de los atributos
new_post={
    "title":"Mi experiencia como dev",
    "content":"la experiencia es tratable",
}
response = requests.post(f"{url}/posts", json=new_post)
print(response.text)

#actualizar post por ID (NO ESTA ACTUALIZANDO LOS DATOS)
update_post={
    "title":"post actualizado",
    "content":"se actualizo el post",
}
response = requests.put(f"{url}/post/2", json=update_post)
print(response.text)

#elimina un post por ID
response = requests.delete(f"{url}/post/2")
print(response.text)

#lista los posts
response = requests.get(f"{url}/posts")
print(response.text)
