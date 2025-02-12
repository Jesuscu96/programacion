from Asignatura import Asignatura
from Estudiante import Estudiante

escuela = []
asignaturas_disponibles = []
def añadir_estudiante(estudiante):
    escuela.append(estudiante)
def listar_estudiantes():
    if not escuela:
        print("No hay estudiantes en la escuela.")
    else:
        for estudiante in escuela:
            print(estudiante)
def buscar_estudiante(nombre):
        for estudiante in escuela:
            if estudiante.nombre.lower() == nombre.lower():
                return estudiante
        return None
# inicio del programa
while True:
    print("\nMenú")
    print("1. Crear Asignaturas")
    print("2. Añadir Estudiante")
    print("3. Listar Estudiantes")
    print("4. Buscar Estudiante por Nombre")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        nombre_asignatura = input("Introduce el nombre de la asignatura: ")
        profesor = input("Introduce el nombre del profesor: ")
        asignatura = Asignatura(nombre_asignatura, profesor)
        asignaturas_disponibles.append(asignatura)
        print(f"Asignatura '{nombre_asignatura}' creada.")
    elif opcion == "2":
        nombre = input("Introduce el nombre del estudiante: ")
        edad = int(input("Introduce la edad del estudiante: "))
        estudiante = Estudiante(nombre, edad)
        print("Asignaturas disponibles:")
        i= 1
        for asignatura in asignaturas_disponibles:
            print(f"{i}. {asignatura.nombre}")
            i+=1
    while True:
        numero = int(input("Selecciona una asignatura: "))
        estudiante.añadir_asignatura(asignaturas_disponibles[numero - 1])
        opcion = input("¿Quiere introducir otra asignatura? s/n ")
        if opcion == "n":
            break
            añadir_estudiante(estudiante)
            print(f"Estudiante '{nombre}' añadido.")
        elif opcion == "3":
            print(f"\nLista de Estudiantes")
            listar_estudiantes()
        elif opcion == "4":
            nombre_buscar = input("Introduce el nombre del estudiante a buscar: ")
            estudiante = buscar_estudiante(nombre_buscar)
            if estudiante:
                print(f"\nDetalles del Estudiante:\n{estudiante}")
            else:
                print("Estudiante no encontrado.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
