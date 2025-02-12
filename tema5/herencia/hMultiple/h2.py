'''Una empresa fabrica productos utilizando exclusivamente maderas y hierros como materiales base.
Diseña un programa utilizando herencia para reflejar que todos los productos de la empresa, deben estar hechos de
estos dos tipos de materiales.
De las maderas queremos saber el tipo de madera (por ejemplo, "roble", "pino") y su resistencia Nivel de resistencia
de la madera (1 a 10),
De los hierros queremos saber la pureza(Porcentaje de pureza del hierro (0 a 100)) y su dureza ( Nivel de dureza del
hierro (1 a 10).)
De la clase producto queremos saber el nombre y el precio.
Clase Producto: Hereda de Madera y Hierro (herencia múltiple).
Atributos:
nombre (string): Nombre del producto.
precio (float): Precio del producto.
Métodos:
__init__(self, nombre, precio, tipo_material, resistencia_o_dureza, pureza=None):
De madera, usa tipo_material y resistencia_o_dureza.
De hierro, usa pureza y resistencia_o_dureza.
descripcion_completa(self): Devuelve una descripción detallada del producto y del material utilizado.
Objetivo del Programa:
Crear una lista de objetos Producto, hechos de madera y hierro.
Crea un menú:
1. Añade objetos Producto a la lista.
2. Mostrar la descripción completa de todos los productos.
3. Mostrar la descripción completa del producto indicado.'''
