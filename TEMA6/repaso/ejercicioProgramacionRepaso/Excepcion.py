class NombreEncontrado(Exception):
    def __init__(self, mensaje="Nombre encontrado"):
        super().__init__(mensaje)

class DiaPosterior(Exception):
    def __init__(self, mensaje="Una persona no puede haber visto la pelicula más tarde que hoy"):
        super().__init__(mensaje)

class FicheroNoEncontrado(Exception):
    def __init__(self, mensaje="Fichero no existe"):
        super().__init__(mensaje)