libro = []
class Libro:
    def __init__(self, titulo, autor, anio_publicacion, disponible):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True
    
    def prestar(self):
        libro_encontrado = False
        for libro in biblioteca:
            if libro.titulo == titulo
            libro_encontrado = True
            libro.prestar_libro()
            break
        if not libro_encontrado:
           print("No se a encontrado el libro.")
           







while True:

    print("Op.1 Agregar un libro.")
    print("Op.2 Prestar un libro.")
    print("Op.3 Devolver un libro.")
    print("Op.4 Mostrar catálogo.")
    print("Op.5 Fin del programa.")

    op = int(input("Introduce la opción: "))

    match op:
        
        case 1:
           
        case 2:
            titulo = str(input("introduce el titulo"))
        case 3:

        case 4:

        case 5:
            print("Fin del programa")
            break
        case _:
            print("Opcion no valida o incorrecta.")