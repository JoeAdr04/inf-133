import requests
##definir la consulta de graphql
query = """ {
    hello
}"""

#definir la  ULR del servidor GraphQL
url = 'http://localhost:8000/graphql'

#solicitud post al serevidor graphql
response = requests.post(url, json={'query': query})
print(response.text)    