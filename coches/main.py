

class Automovil:

    def __init__(self, marca, modelo, color, vel_max):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.vel_max = vel_max
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad máxima: {self.vel_max}"
    
coche1 = Automovil("bmw","m3", "negro", 270)
coche2 = Automovil("Mercedes", "Clase C","Rojo" ,240)
coche3 = Automovil("Ford", "Focus", "azul", 220)


lista = [coche2, coche1, coche3]

for coche in lista:
    print(coche)


