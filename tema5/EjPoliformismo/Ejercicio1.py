'''Partiendo del un diagrama de clases en el que tenemos una clase animal, 
que tiene como clases hijas:
perros y gatos. Implementa estas clases para poder utilizarlas en 
una lista ConjuntoMascotas.
Crea un menú para:
• Añadir animales a la lista.
• Muestra todas las propiedades de cada uno de los objetos de la lista.'''
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")

CojuntoMascotas = []

while True:
    print("Op1 Añanade un animal.")
    print("Op2 Muestra todas las propiedades de cada uno de los objetos de la lista.")
    print("Op3 Fin del programa")
    
    op = str(input("Introduce la opción que desees 1,2 o 3"))
    match op:
        case "1":
            animal = str(input("Añade un animal perro o gato"))
            CojuntoMascotas.append(animal())
        case "2":
            print(f"{CojuntoMascotas}")
        case "3":
            print("Fin del programa.")
            break
        case _:
            print("Ingresa bien los caracteres numericos.")