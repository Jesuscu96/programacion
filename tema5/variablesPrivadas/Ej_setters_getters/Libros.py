class Libro:
    #Atributo privado
    def __init__(self, titulo, autor, isbn, prestado):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._prestado = prestado 
    #getter
    @property # Camuflo el atributo
    def titulo(self):
        return self._titulo
    @property
    def autor(self):
        return self._autor
    @property
    def isbn(self):
        return self._isbn
    @property
    def prestado(self):
        return self._prestado
    #setter
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    @autor.setter
    def autor(self, autor):
        self._autor = autor
    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn
    @prestado.prestado
    def prestado(self, prestado):
        self._prestado
    
    def mostrar_informacion(self):
        if self._prestado:
            prestado_str = "Sí"
        else: prestado_str = "No"
        return f"Titulo: {self._titulo}, Autor: {self._autor}, Isbn: {self._isbn}, Prestado: {self._prestado}"
    