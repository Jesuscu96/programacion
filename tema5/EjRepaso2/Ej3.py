class Libro:
    def __init__(self, titulo, autor, anio_publicacion, disponible):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible
    
    def prestar(self):
        if