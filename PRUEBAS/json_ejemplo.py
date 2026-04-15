import json

alumno = {
    "nombre": "Alve",
    "nota": 9,
    "nombre1": "Yo",
    "nota1": 10
}


# Guardar
with open("datos.json", "w") as archivo:
    json.dump(alumno,archivo)


# Leer
with open("datos.json", "r") as archivo:
    datos = json.load(archivo)

print(f"{datos['nombre']} tiene {datos['nota']}")
print(f"{datos['nombre1']} tiene {datos['nota1']}")
