
class Nota:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def ha_pasado(self):
        if self.nota >= 75:
            ap = "aprobado"
        else:
            ap = "suspendido"
        print(f"El/La estudiante {self.nombre} ha {ap}")
nota_1 = Nota("Julian", 80)
nota_1.ha_pasado()
nota_2 = Nota("Oscar", 40)
nota_2.ha_pasado()
