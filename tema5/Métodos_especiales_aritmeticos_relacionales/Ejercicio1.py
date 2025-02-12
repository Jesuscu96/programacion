class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def __str__(self):
        return f"Rectangulo de ancho {self.ancho} y alto {self.alto}"
    
    def __add__(self, other):
        return Rectangulo(self.ancho + other.ancho, self.alto + other.alto)
    
    def __lt__(self, other):
        return self.ancho * self.alto < other.ancho * other.alto
    def __eq__(self, other):
        return
        