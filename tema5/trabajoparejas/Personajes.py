from abc import ABC, abstractmethod
# Jesús Clemente & Alejandro Perales

class Personaje(ABC):
    def __init__(self, nombre, vida, ataque):
        # Inicialización de los atributos comunes para todos los personajes
        self._nombre = nombre
        self._vida = vida
        self._ataque = ataque
        self.__experiencia = 0  # La experiencia es privada

    def ganar_experiencia(self):
        # Incrementa la experiencia en 10 puntos por acción
        self.__experiencia += 10

    def ver_experiencia(self):
        # Devuelve la experiencia acumulada del personaje
        return f"Experiencia de {self._nombre}: {self.__experiencia} puntos"

    @abstractmethod
    def dar_golpe(self):
        # Método abstracto para implementar cómo un personaje da un golpe
        pass

    @abstractmethod
    def recibir_golpe(self, golpe):
        # Método abstracto para implementar cómo un personaje recibe un golpe
        pass

    @abstractmethod
    def ver_datos(self):
        # Método abstracto para mostrar los datos del personaje
        pass