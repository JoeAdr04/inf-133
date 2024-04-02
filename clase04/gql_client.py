import requests 
#definir  la consulta graphql
query = """
    {
        estudiante{
            
            nombre
            apellido
            
        }
    """
query_lista = """
{
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""

query = """
    {
        estudiantePorId(id: 2){
            nombre
        }
    }
"""
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)