import requests

URL = "https://pokeapi.co/api/v2/pokemon/"

pokemon = input("Ingrese el nombre de un pokemon: ")

respuesta = requests.get(URL + pokemon)
datos = respuesta.json()

print(f"Movimientos de {pokemon}: ")

for move in datos["moves"]:
    print(move["move"]["name"])

for type in datos["types"]:
    print(type["type"]["name"])

# get, recuperar informacion del servidor (solo lectura)
# post, enviar informacion al servidor
# put, actualizar informacion existente en el servidorch
# delete, eliminar informacion del servidor