from abc import ABC, abstractmethod

# Definimos la interfaz Habilidades he incluimos el abstractmethod
class Habilidades(ABC):
    @abstractmethod
    def dar_golpe(self):
        pass

    @abstractmethod
    def recibir_golpe(self):
        pass

    @abstractmethod
    def ver_datos(self):
        pass

# Ahora la clase Personaje implementará la interfaz Habilidades
class Personaje(Habilidades):
    def __init__(self, nombre, vida, ataque):
        self._nombre = nombre  # variables protegidas
        self._vida = vida
        self._ataque = ataque
        self.__experiencia = 0  # variable privada

    def ganar_experiencia(self):
        self.__experiencia += 10  # sumas 10 puntitos de XP

    def ver_experencia(self):
        return f"Experiencia de {self._nombre}: {self.__experiencia} puntos"

    # Aunque Habilidades define estos métodos, los dejamos vacíos en la clase base
    @abstractmethod
    def dar_golpe(self):
        pass

    @abstractmethod
    def recibir_golpe(self):
        pass

    @abstractmethod
    def ver_datos(self):
        pass


class Mago(Personaje):
    fuego = 5   #distintas variables de hechizos para magos 
    hielo = 10
    electrico = 15

    def __init__(self, nombre, vida, ataque, hechizo):
        super().__init__(nombre, vida, ataque)
        self._hechizo = hechizo

    def dar_golpe(self):
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
        self._vida -= golpe
        if self._vida < 0:
            self._vida = 0

    def ver_datos(self):
        return f"Nombre: {self._nombre} | Vida: {self._vida} | Hechizo: {self._hechizo}"


class Caballero(Personaje):
    escudo = 20

    def __init__(self, nombre, vida, ataque):
        super().__init__(nombre, vida, ataque)
        self._escudo = Caballero.escudo

    def dar_golpe(self):
        self.ganar_experiencia()
        return self._ataque

    def recibir_golpe(self, golpe):
        if self._escudo >= golpe:
            self._escudo -= golpe
        else:
            golpe -= self._escudo
            self._escudo = 0
            self._vida -= golpe
            if self._vida < 0:
                self._vida = 0

    def ver_datos(self):
        return f"Nombre: {self._nombre} | Vida: {self._vida} | Escudo: {self._escudo}"

# Creación de los personajes
personaje_1 = Mago("Gandalf", 80, 40, "hielo")
personaje_2 = Caballero("Aragon", 100, 40)

# Simulación del combate
for i in range(1, 4):  # tres turnos de combate
    if i % 2 != 0:
        golpe = personaje_1.dar_golpe()
        personaje_2.recibir_golpe(golpe)
        print(f"{personaje_1._nombre} ataca con {golpe} de daño")
    else:
        golpe = personaje_2.dar_golpe()
        personaje_1.recibir_golpe(golpe)
        print(f"{personaje_2._nombre} ataca con {golpe} de daño")
    
    print(personaje_1.ver_datos())
    print(personaje_2.ver_datos())

print(personaje_1.ver_experencia())
print(personaje_2.ver_experencia())