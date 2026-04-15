class Persona:
    def __init__(self, nombre, edad):
        self.nombre = "Jordiiiiiii"
        self.edad = 21

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

persona1 = Persona("Jordi", 21)
persona1.saludar()

#Ejemplo
class Auto:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año

    def mostrar_info(self):
        print(f"Auto: {self.marca} - Año: {self.año}")

auto1 = Auto("Toyota", 2022)
auto1.mostrar_info()
auto2= Auto("Ferrari", 2026)
auto2.mostrar_info()

#Mi ejemplo
class alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def notas(self):
            print(f"Mi nombre es {self.nombre} mi nota es de {self.nota}")

alumno1 = alumno("Jordi", 9.5)
alumno1.notas()
alumno2 = alumno("Mayra", 7)
alumno2.notas()

#ejemplo corregido y mas elegante agregando si aprueba o no
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
   
    def mostrar_nota(self):
        print(f"{self.nombre} tiene una nota de {self.nota}")
    def aprobo(self):
        if self.nota >=7:
            print("Aprobado")
        else:
            print("Reprobado")

alumno1 = Alumno("Jordi", 9.5)
alumno1.mostrar_nota()
alumno1.aprobo()
alumno2 = Alumno("Mayra", 7)
alumno2.mostrar_nota()
alumno2.aprobo()
alumno3 = Alumno("Alexander", 6.99)
alumno3.mostrar_nota()
alumno3.aprobo()

#Mas sencillo
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
   
    def mostrar_nota(self):
        print(f"{self.nombre} tiene una nota de {self.nota}")
    def aprobo(self):
        if self.nota >=7:
            return "Aprobado"
        else:
            return "Reprobado"

alumno1 = Alumno("Jordi", 9.5)
print(f"El alumno {alumno1.nombre} esta {alumno1.aprobo()} con una nota de {alumno1.nota}")
alumno2 = Alumno("Mayra", 7)
print(f"El alumno {alumno2.nombre} esta {alumno2.aprobo()} con una nota de {alumno2.nota}")
alumno3 = Alumno("Alexander", 6.99)
print(f"El alumno {alumno3.nombre} esta {alumno3.aprobo()} con una nota de {alumno3.nota}")

#Codigo con listas 
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
   
    def aprobo(self):
        if self.nota >= 7:
            return "Aprobado"
        else:
            return "Reprobado"

    def excelente(self):
        if self.nota >= 9:
            return "Excelente"
        else:
            return "Normal"

alumnos = [
    Alumno("JordiII", 9.5),
    Alumno("Mayra", 7),
    Alumno("Alexander", 6.99),
    Alumno("Messi",10),
    Alumno("Amadeus",7),
    Alumno("Añañin",5)
]

for estudiante in alumnos:
    estado = estudiante.aprobo()
    if estado == "Aprobado":
        print(f"El alumno {estudiante.nombre} esta {estado} con una nota de {estudiante.nota} {estudiante.excelente()}")
    else:
        print(f"El alumno {estudiante.nombre} esta {estado} con una nota de {estudiante.nota}")