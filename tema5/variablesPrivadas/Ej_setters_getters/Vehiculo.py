class Vehiculo:
    def __init__(self, nombre= "sin nombre", velocidad = 0):
        self._nombre = nombre
        self._velocidad = velocidad
    
    def get_nombre(self):
        return self._nombre
    
    def get_velocidad(self):
        return self._velocidad
    