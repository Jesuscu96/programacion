class Bombero:
    def __init__(self, nombre, apellidos, edad, especialista):
        self._nombre = nombre
        self._apellidos = apellidos
        self._edad = edad
        self._especialista = especialista
   #getter posiblemente mal hecho
    def get_nombre(self):
        return self._nombre
    def get_apellidos(self):
        return self._apellidos
    def get_edad(self):
        return self._edad
    def is_especialista(self):
        return self._especialista
    
    #setter
    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_apellidos(self, apellidos):
        self._apellidos = apellidos
    def set_edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("edad no válida")
    def mostrar_informacion(self):
        if self._especialista:
            especialista_str = "Sí"
        else: especialista_str = "No"
        return f"Nombre: {self._nombre}, Apellidos: {self._apellidos}, Edad: {self._edad}, Especialidad: {self._especialista}"
    