class Productos:
    cantidad_total = 0
    def __init__(self, codigo_producto, nombre, precio ):
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.precio = precio
        Productos.cantidad_total+=1
    
    def muestra_datos(self):
        return f"Sus datos son nombre {self.nombre}, precio {self.precio}€ y su codigo es {self.codigo_producto}."
    
       
    @classmethod 
    def total_productos(cls):
        return Productos.cantidad_total
    