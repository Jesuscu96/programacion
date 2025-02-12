class SeleccionFutbol:  #Clase Padre
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentrarse(self):
        return f"{self.nombre} {self.apellidos} -> Concentrase"
    
    def viajar(self):
        return f"{self.nombre} {self.apellidos} -> Viajar"
    
    def entrenamiento(self):
        return f"{self.nombre} {self.apellidos} -> Estan en el entrenamineto"
    
    def partido(self):
        return f"{self.nombre} {self.apellidos} -> Esta en el partido"
    
    
class Futbolista(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion
    
    def entrenamiento(self):
        return f"{self.nombre} {self.apellidos} -> Realiza un entrenamiento"
    
    def partido(self):
        return f"{self.nombre} {self.apellidos} -> Juega un partido"
    
    def entrevista(self):
        return f"{self.nombre} {self.apellidos} -> Da una Entrevista"
    
class Entrenador(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, idFederacion, planifcar):
        super().__init__(id, nombre, apellidos, edad)
        self.idFederacio = idFederacion
        self.planificar = planifcar
    
    def entrenamiento(self):
        return f"{self.nombre} {self.apellidos} -> Dirige un entrenamineto"
    
    def partido(self):
        return f"{self.nombre} {self.apellidos} -> Dirige un partido"
    
    def planificarEntrenamiento(self):
        return f"{self.nombre} {self.apellidos} -> Planificar un Entrenamineto"
    
     
class Masajista(SeleccionFutbol):
    def __init__(self, id, nombre, apellidos, edad, titulacion, aniosExp):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.aniosExp = aniosExp
    
    def entrenamiento(self):
        return f"{self.nombre} {self.apellidos} -> Da asistencia en el entrenamiento"
    
    def partido(self):
        return f"{self.nombre} {self.apellidos} -> Asiste al partido de futbol"

    def masaje(self):
        return f"{self.nombre} {self.apellidos} -> Da un Masaje"
#Instancias

futbolista1 = Futbolista(1, "Carlos", "Sánchez", 25, 10, "Delantero")
futbolista2 = Futbolista(2, "Luis", "Gómez", 30, 5, "Defensa")
entrenador = Entrenador(3, "Juan", "Pérez", 45, "FED123", True)
masajista = Masajista(4, "Ana", "Martínez", 35, "Licenciada en Fisioterapia", 10)
#LISTA
team = [futbolista1, futbolista2, entrenador, masajista]    

    #MENU
while True:
    print("Op1: Todos los integrantes comienzan una concentración.")
    print("////////////////////////////////////////////////////////////////////")
    print("Op2: Todos los integrantes viajan para jugar un partido.")
    print("////////////////////////////////////////////////////////////////////")
    print("Op3: Todos los integrantes tienen su función en un entrenamiento.")
    print("////////////////////////////////////////////////////////////////////")
    print("Op4: Todos los integrantes tienen su función en un partido.")
    print("////////////////////////////////////////////////////////////////////")
    print("Op5: El jugador sera entrevistado.")
    print("////////////////////////////////////////////////////////////////////")
    print("Op6: El masajista dara una masaje.")
    print("////////////////////////////////////////////////////////////////////")
    print("Op7: Fin del programa.")
    print("////////////////////////////////////////////////////////////////////")
    
    op = str(input("Ingrese el numero que desee 1, 2, 3, 4, 5, 6 o 7: "))

    match op:
        case "1":
            for miembro in team:
                print(miembro.concetrarse())
        case "2":
            for miembro in team:
                print(miembro.viajar())
        case "3":
            for miembro in team:
                print(miembro.entrenamiento())
        case "4":
            for miembro in team:
                print(miembro.partido())
        case "5":
            if isinstance(futbolista1, Futbolista):  # Example: Interview the player
                print(futbolista1.entrevista())
        case "6":
            if isinstance(masajista, Masajista):
                print(masajista.masaje())
        case "7":
            print("Fin del programa.")
            break
        case _:
            print("Opción inválida. Intente nuevamente.")