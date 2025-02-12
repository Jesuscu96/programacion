class Libro:
    def __init__(self, titulo, nombre, precio):
        self.titulo = titulo
        self.nombre = nombre
        self.precio = precio
    def mostrar (self):
        print(f"El titulo del libro es {self.titulo} y el autor es {self.nombre} con un precio de {self.precio}")
libro_1 = Libro("El señor de los anillos", "Petter Jackson", "20€")
libro_1.mostrar() 