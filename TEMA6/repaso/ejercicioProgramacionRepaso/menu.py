from agregar import agregarUsuario
from navegador import navegador
from mostrarNombres import mostrarNombres
def menu():
    while True:
        print(f"\n---Menu ejercicio en txt---\n1-Agregar cinéfilo\n2-Mostrar todos los nombres\n3-Mostrar fichero en navegador\n4-Borrar cinéfilo\n5-Salir")
        opcion=input("Dime la opcion que quieras: ")
        match opcion:
            case "1":
                agregarUsuario()
            case "2":
                mostrarNombres()
            case "3":
                navegador()
            case "4":
                pass
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion incorrecta")