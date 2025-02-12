class Semaforo:
    def __init__(self, color="rojo"):
        self._color = None # Atributo privado para almacenar el color
        self.color = color # Asignar el color inicial usando el setter
    @property # Getter para el atributo color
    def color(self):
        return self._color
    @color.setter # Setter para el atributo color con validación
    def color(self, nuevo_color):
        colores_validos = ["rojo", "amarillo", "verde"]
        if nuevo_color not in colores_validos:
            print("Lo sentimos, el color no es valido")
        else: 
            self._color = nuevo_color
    def mostrar_estado(self): # Método para mostrar el estado del semáforo
        return f"El semáforo está en {self.color}."
