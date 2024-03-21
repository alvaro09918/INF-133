#falta cactualizar y eliminar post

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

#lista los posts
response = requests.get(f"{url}/posts")
print(response.text)


