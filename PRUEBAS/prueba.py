#INCIO
nombre = "Jordi"
edad = 21

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
#BUCLE
for i in range(5):
    print(i)
#LISTAS
numeros= [1,2,3,4,5]
for n in numeros:
    print(n)
#EJEMPLO
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
#Practica
nombre ="Jordi"
for j in range(1,6):
    print(f"{nombre} - {j}")
#Parctica 2
nombre ="Jordi"
for l in range(1,6):
    if l %2 == 0:
        print(f"{nombre} - {l}")
