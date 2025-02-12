from Personajes import Personaje

from Habilidad import Habilidades
class Caballero(Personaje, Habilidades):
    # Daño que puede absorber el escudo
    escudo = 20

    def __init__(self, nombre, vida, ataque):
        # Inicializa el caballero con un escudo por defecto
        super().__init__(nombre, vida, ataque)
        self._escudo = Caballero.escudo

    def dar_golpe(self):
        # El caballero ataca y gana experiencia
        self.ganar_experiencia()
        return self._ataque

    def recibir_golpe(self, golpe):
        # El caballero recibe daño, primero se consume el escudo
        if self._escudo >= golpe:
            self._escudo -= golpe
        else:
            golpe -= self._escudo
            self._escudo = 0
            self._vida -= golpe
            if self._vida < 0:
                self._vida = 0

    def ver_datos(self):
        # Devuelve la información actual del caballero, incluyendo el escudo
        return f"Nombre: {self._nombre} | Vida: {self._vida} | Escudo: {self._escudo}"

    def habilidad_especial(self):
        # Habilidad especial del caballero: reforzar el escudo
        self._escudo += 15
        print(f"{self._nombre} refuerza su escudo y gana 15 puntos de escudo.")