from abc import ABC, abstractmethod

# Interfaz para definir habilidades
class Habilidades(ABC):
    @abstractmethod
    def habilidad_especial(self):
        pass