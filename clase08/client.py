import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

response = requests.get(url)
print(response.json())

mi_taco = {
    "base": "tortilla",
    "guiso": "frijoles",
    "salsa": "chilaquiles",
    "toppings": ["carnita", "chicharon","espinacas"]
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())


response = requests.get(url)
print(response.json())


edit_taco = {
    "base": "torta",
    "guiso": "aji",
    "salsa": "picante",
    "toppings": ["espinacas", "choclo"]
}
response = requests.post(url, json=edit_taco, headers=headers)
print(response.json())

response = requests.get(url)
print(response.json())


response = requests.delete(url + "/1")
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())
