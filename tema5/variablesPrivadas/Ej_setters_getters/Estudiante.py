class Estudiante:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        self._asignaturas = []

    @property # Camuflo el atributo
    def nombre(self):  #getter
        return self._nombre
    @property
    def edad(self):
        return self._edad
    @property
    def asignaturas(self):
        return self._asignaturas
   
    @nombre.setter #setter
    def nombre(self, nombre): 
        self._nombre = nombre
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    @asignaturas.setter
    def asiganaturas(self, asignaturas):
        self._asignaturas = asignaturas
    
    
    def añadir_asignatura(self, asignatura):
        self._asignaturas.append(asignatura)
    def __str__(self):
        asignaturas_str=""
        for asignatura in self._asignaturas:
            asignaturas_str = asignaturas_str + "\n " + asignatura.nombre
        return f"Nombre: {self._nombre}, Edad: {self._edad}\n Asignaturas: {asignaturas_str}"
