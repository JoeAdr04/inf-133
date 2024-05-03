import requests

url = 'http://localhost:5000/'

response = requests.get(url)

if response.status_code == 200:
    print("respuesta del servidor")
    print(response.text)
else:
    print("error al conectar o  el servidor: ", response.status_code)

params = {"nombre": 'Joel'}
response  = requests.get(url+'saludar', params=params)

if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

params = {"num1": 5, "num2": 3}
response = requests.get(url+'sumar', params=params)

if response.status_code == 200:
    data = response.json()
    mensaje = data['sumar']
    print("respuesta del servifot(GET):", mensaje)
else:
    print("error al conectar con el servidor(GET):", response.status_code)