class Empleado:
    def __init__(self, nombre, apellido, salario, puesto, departamento):
        self._nombre = nombre
        self._apellido = apellido
        self.__salario = salario
        self._puesto = puesto
        self._departamento = departamento

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_apellido(self):
        return self._apellido
    
    def set_nombre(self, apellido):
        self._apellido = apellido
    
    @property
    def salario(self):
        return self.__salario 
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    def get_puesto(self):
        return self._puesto
    
    def set_puesto(self, puesto):
        self._puesto = puesto

    def get_departamento(self):
        return self._departamento
    
    def set_departamento(self, departamento):
        self._departamento = departamento
    
    def aumentar_salario(self):
         self.salario *= 1.10
    def motrar_info(self):
        return f"Su datos son nombre: {self.get_nombre()}, apellidos: {self.get_apellido()}, salario: {self.salario}, puesto: {self.get_puesto()}, departamento: {self.get_departamento()}"
    
empleado1 = Empleado("Juan", "Gomez", 1000, "asesor", "marketing")
empleado1.aumentar_salario()
print(empleado1.motrar_info())