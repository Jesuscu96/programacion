
import math

class Circulo:
    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.R = R
    def area (self): 
        c_area = math.pi * (self.R * self.R)
        print("El area del cilculo es {:.2f} cm^2.".format(c_area))
    
    def perimetro (self):
        d = self.R * 2 
        c_perimetro = d * math.pi
        print("El perimetro del circilo son {:.2f} cm.".format(c_perimetro) )
    
    def mostrar_propiedades(self):
        print(f"Las cordenadas de su centro O son {self.x}, {self.y} y tiene un radio de {self.R} cm.")

Circulo_1 = Circulo (3, 4, 5)
Circulo_1.mostrar_propiedades()
Circulo_1.area()
Circulo_1.perimetro()
