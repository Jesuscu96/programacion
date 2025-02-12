class Vehiculo:
    def __init__(self, marca, velocidad_inicial=0):
        self.marca = marca
        self.velocidad_inicial = velocidad_inicial
    
    def acelerar(self, velocidad_inicial):
        if self.velocidad_inicial >0:
            print(f" El coche esta acelerando su velocidad es {self.velocidad_inicial}")
    
    def desacelerar(self, velocidad_inicial):
        if self.velocidad_inicial <0:
            print(f"El coche es desacelerando su velocidad es {self.velocidad_inicial}")

    def mostrar(self,velocidad_inicial)
        print(f"Su velociadad actual es {self.velocidad_inicial}")
    
class Coche (Vehiculo):
    def __init__(self, marca, velocidad_inicial):
        Vehiculo.__init__(self, marca, velocidad_inicial, bocina="Pi_Pi!!")
        self.bocina = "Pi_Pi!!"
    def klaxonner(self):
        return self.bocina
coche_1 = Coche("Peugeot 208", 10.5)
print (f"Caracteristicas del coche {coche_1}") ## a completar
coche_1.acelerar(50)
coche_1.desacelerar(15)
coche_1.mostrar()
coche_1.klaxonner()
    
