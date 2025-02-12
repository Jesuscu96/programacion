class Cliente:
    cantidad_total = 0
    def __init__(self,numero, nombre, apellidos ,nivel):
        self.numero = numero
        self.nombre = nombre
        self.apellidos = apellidos
        self.nivel = nivel
        Cliente.cantidad_total+=1
    
    def nombre_cliente(self):
       return f"El nombre del cliente es {self.nombre}" 
    def muestra_datos(self):
        return f"y sus datos son nombre {self.nombre} apellidos {self.apellidos} numero {self.numero} y su nivel es {self.nivel} "
       
    @classmethod 
    def total_clientes_actual(cls):
        return Cliente.cantidad_total
