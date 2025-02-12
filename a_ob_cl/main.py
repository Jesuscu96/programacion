#1- Utilizando objetos literales, crea un objeto con las propiedades nombre, edad y estadoCivil, con los siguientes datos:
#Luis Vargas, 21 años y soltero.
#Carmen Perez, 32 años, soltera.
#Andrés Iglesias, 24 años, casado

'''class Persona:
    def __init__(self, nombre, edad, e_civil):
        self.nombre = nombre
        self.edad = edad 
        self.e_civil = e_civil
    def __str__(self):
        nombre = f"nombre: {self.nombre}"
        edad = f"Edad: {self.edad}"
        return f"{nombre}\n{edad}"
    


usuario1 = Persona("Luis", 22, "soltero")
ususario2 = Persona("Carmen", 32, "soltero")
lista = [usuario1.nombre, ususario2.nombre]
print(lista)
#print(usuario1)'''
lista=[]
class Estudiante:
    def __init__(self, nombre, grupo, nota, practica):
        self.nombre = nombre
        self.grupo = grupo 
        self.nota = nota
        self.practica = practica
    def __str__(self):
        return f"Nombre: {self.nombre}"
    
def agregar():
    nombre = str(input("Introduzca el nombre del estudiante: "))
    grupo = str(input("Introduzaca el grupo según estas opciones (a,b,c,d): "))
    nota = float(input("Introduzca la nota: "))
    practica = str(input("Introduza con un si o un no si aprobado la practica: "))
    return Estudiante(nombre, grupo, nota, practica)
def lee(lista):
    estudiante = agregar()
    lista.append(estudiante)
#lee(lista)

class Coche:

    def __init__(self):
        
        
        

