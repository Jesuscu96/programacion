from abc import ABC, abstractmethod
class Edificio(ABC):
    contador = 0
    def __init__(self,ascensores):
        self._ascensores = ascensores
        contador += 1
        
    @abstractmethod
    def hallar_impuesto(self):
        pass
    
    
