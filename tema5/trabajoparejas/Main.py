# Jesús Clemente & Alejandro Perales
from Personajes import Personaje
from Magos import Mago
from Caballeros import Caballero
from Habilidad import Habilidades



# Calse es para reiniciar los personajes a su estado inicial
# manteniendo la experiencia acumulada
class Reiniciar:
    def reiniciar_personajes():
        global personaje_1, personaje_2

        # Guardar la experiencia actual antes de reiniciar
        experiencia_mago = personaje_1._Personaje__experiencia if 'personaje_1' in globals() else 0
        experiencia_caballero = personaje_2._Personaje__experiencia if 'personaje_2' in globals() else 0

        # Crear nuevos personajes manteniendo la experiencia acumulada
        personaje_1 = Mago("Gandalf", 80, 40, "fuego")
        personaje_1._Personaje__experiencia = experiencia_mago

        personaje_2 = Caballero("Aragorn", 100, 40)
        personaje_2._Personaje__experiencia = experiencia_caballero

# Creamos personajes iniciales
Reiniciar.reiniciar_personajes()
print("¡¡Normas un ataque por turno, Gandalf podra cambiar el hechizo cuando quiera ilimitamente y la habilidad especial es de un unico uso!!.")
# Las normas del juego se pueden modificar a gusto de los jugares según quieran los juagadores

# Menú interactivo
while True:
    print("\n--- Menú de combate ---")
    print("1. Atacar y ver datos de Gandalf (Mago)")
    print("2. Atacar y ver datos de Aragorn (Caballero)")
    print("3. Elegir hechizo de Gandalf")
    print("4. Simular un combate")
    print("5. Ver experiencia de los personajes")
    print("6. Habilidad especial de Gandalf (Mago)")
    print("7. Habilidad especial de Aragorn (Caballero)")
    print("8. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            # El mago ataca al caballero y se muestran sus datos
            golpe = personaje_1.dar_golpe()
            personaje_2.recibir_golpe(golpe)
            print(f"{personaje_1._nombre} ataca con {golpe} de daño")
            print(personaje_1.ver_datos())
            print(personaje_2.ver_datos())

        case "2":
            # El caballero ataca al mago y se muestran sus datos
            golpe = personaje_2.dar_golpe()
            personaje_1.recibir_golpe(golpe)
            print(f"{personaje_2._nombre} ataca con {golpe} de daño")
            print(personaje_1.ver_datos())
            print(personaje_2.ver_datos())

        case "3":
            # Permite elegir un hechizo para el mago
            hechizo = input("Elige un hechizo (fuego, hielo, electrico): ").lower()
            personaje_1.elegir_hechizo(hechizo)

        case "4":
            # Simulación de combate automático
            for i in range(1, 4):
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

            print(personaje_1.ver_experiencia())
            print(personaje_2.ver_experiencia())

        case "5":
            # Muestra la experiencia acumulada de ambos personajes
            print(personaje_1.ver_experiencia())
            print(personaje_2.ver_experiencia())

        case "6":
            # Activar habilidad especial del mago
            personaje_1.habilidad_especial()

        case "7":
            # Activar habilidad especial del caballero
            personaje_2.habilidad_especial()

        case "8":
            # Finalizar el juego
            print("Saliendo del juego...")
            break

        case _:
            # En caso de error
            print("Opción no válida. Por favor, elige una opción del menú.")
