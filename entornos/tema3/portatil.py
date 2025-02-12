'''class Portatil:
    def __init__(self, marca, velocidad, ram, hd, cargado):
        self.marca = marca
        self.velocidad = velocidad
        self.hd = hd
        self.ram = ram
        self.cargado = cargado

    def memoria(self):
        self.ram += 16
    def cargar(self):
        self.carga = 100
    def del_marca(self):
        return self.marca
portatil_1 = Portatil("Asus", 4.5, 16, 1000, 0)  
portatil_1.memoria()
portatil_1.cargar()
portatil_1.del_marca()
print(f"Las especificaciones del portatil son marca {self.marca}, velocidad del procesador {self.velocidad}Ghz, memorira ram {self.ram}Gb, tamaño del hd {self.hd} y su porcentaje de carga de la bateria {self.cargado}% ")'''
class Portatil:
    def __init__(self, marca, velocidad, ram, hd, cargado=0):
        self.marca = marca
        self.velocidad = velocidad
        self.hd = hd
        self.ram = ram
        self.cargado = cargado

    def memoria(self):
        self.ram += 16  
    
    def cargar(self):
        self.cargado += 100  
    
    def del_marca(self):
        return self.marca  


portatil_1 = Portatil("Asus", 4.5, 16, 1000, 0)


portatil_1.memoria()  
portatil_1.cargar()
portatil_1.del_marca()


print(f"Las especificaciones del portátil son: marca {portatil_1.marca}, "
      f"velocidad del procesador {portatil_1.velocidad} GHz, "
      f"memoria RAM {portatil_1.ram} GB, tamaño del HD {portatil_1.hd} GB, "
      f"y su porcentaje de carga de la batería {portatil_1.cargado}%.")      