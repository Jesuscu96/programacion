class Empleado:
  def __init__(self,nombre,edad):
    self.nombre=nombre
    self.edad=edad
    print(f"¡El empleado llamado {self.nombre} y de {self.edad} años ha sido creado!")
  def __del__(self):
    print(f"¡El destructor ha sido llamado, el empleado llamado {self.nombre} ha sido eliminado!")
empleado_1 = Empleado("Martin",26)
empleado_2 = Empleado("Jose", 24)
del empleado_1
del empleado_2