from Personajes import Personaje
from Habilidad import Habilidades


class Mago(Personaje, Habilidades):
    # Daños base de los hechizos del mago
    fuego = 5
    hielo = 10
    electrico = 15

    def __init__(self, nombre, vida, ataque, hechizo="fuego"):
        # Inicializa el mago con un hechizo por defecto
        super().__init__(nombre, vida, ataque)
        self._hechizo = hechizo

    def elegir_hechizo(self, hechizo):
        # Permite al mago elegir un hechizo válido
        if hechizo in ["fuego", "hielo", "electrico"]:
            self._hechizo = hechizo
            print(f"Hechizo seleccionado: {hechizo}")
        else:
            print("Hechizo no válido, manteniendo el hechizo actual.")

    def dar_golpe(self):
        # El mago ataca y gana experiencia
        self.ganar_experiencia()
        if self._hechizo == "fuego":
            return self._ataque + Mago.fuego
        elif self._hechizo == "hielo":
            return self._ataque + Mago.hielo
        elif self._hechizo == "electrico":
            return self._ataque + Mago.electrico
        else:
            print("Este hechizo está mal conjurado")
            return self._ataque

    def recibir_golpe(self, golpe):
        # El mago recibe daño en su vida
        self._vida -= golpe
        if self._vida < 0:
            self._vida = 0

    def ver_datos(self):
        # Devuelve la información actual del mago
        return f"Nombre: {self._nombre} | Vida: {self._vida} | Hechizo: {self._hechizo}"

    def habilidad_especial(self):
        # Habilidad especial del mago: recuperar vida con magia
        self._vida += 20
        print(f"{self._nombre} usa magia curativa y recupera 20 puntos de vida.")
