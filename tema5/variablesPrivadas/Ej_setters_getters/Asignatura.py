class Asignatura:
    def __init__(self, nombre, profesor):
        self._nombre = nombre
        self._profesor = profesor
    @property # Camuflo el atributo
    def nombre(self):  #getter
        return self._nombre
    
    @property
    def profesor(self): #getter
        return self._profesor
    
    @nombre.setter
    def nombre(self, nombre): #setter
        self._nombre = nombre

    @profesor.setter
    def profesor(self, profesor):
        self._profesor = profesor
        
    def __str__(self):
        return f"Asignatura: {self._nombre}, Profesor: {self._profesor}"
    