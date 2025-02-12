class Empleado:
  def __init__(self,nombre, funcion, edad):
    self.nombre = nombre
    self.funcion = funcion
    self.edad = edad
    print(f"¡El empleado llamado {self.nombre} y de {self.edad} años ha sido creado!")
  
  def trabajar (self, numero_horas):
