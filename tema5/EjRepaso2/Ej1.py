class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar (self):
        return f"El nombre es {self.nombre} y su edad es {self.edad}. "
    def __str__(self):
        cadena = self.nombre + " , " + str(self.edad)
        return cadena

persona1 = Persona("Juan", 22)
persona2 = Persona("Jesús", 28)

print(persona1.saludar())
print(persona2.saludar())
print(str(persona1) + " - " + str(persona2))