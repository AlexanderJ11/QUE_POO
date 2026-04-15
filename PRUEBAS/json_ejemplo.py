import json

alumno = [
    { "nombre": "Jordi", "edad": 21, "notas":8,},
    { "nombre": "Messi", "edad": 38, "notas": 7},
    {"nombre": "CR7", "edad": 40, "notas": 5},
    {"nombre": "Alexander", "edad": 17, "notas": 10},
    {"nombre": "KENY", "edad": 11, "notas": 6.99},
]


# Guardar
with open("datos.json", "w") as archivo:
    json.dump(alumno,archivo)


# Leer
with open("datos.json", "r") as archivo:
    datos = json.load(archivo)

for alumnos in datos:
    #VERIFICAR EDAD
    if alumnos["edad"] >= 18:
        estado = "ES MAYOR DE EDAD"
    else:
        estado = "ES MENOR DE EDAD"
    #PROMEDIO DE NOTAS
    if alumnos["notas"] >=6.99:
        promedio = "SE ENCUENTRA APROBADO"
    else:
        promedio = "SE ENCUNETRTA REPROBADO"

    print(f"{alumnos['nombre']} tiene {alumnos['edad']} años - {estado} con una nota de {alumnos["notas"]} - {promedio}")

