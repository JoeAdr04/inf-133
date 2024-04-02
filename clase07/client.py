import requests

url = "http://localhost:8000"




response = requests.get(f"{url}/posts")

print(response.text)

ruta_get = url + "posts/2"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)