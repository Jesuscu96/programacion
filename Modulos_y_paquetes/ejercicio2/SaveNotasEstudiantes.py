

SaveNotasEstudiantes = __name__
from notas_estudiantes import gestor_notas
estudiantes={}

while True:
    # indicaciones del menu
    print("-----------------------------------------------------------------------------")
    print("1 Opción agrear una nota se le solicitara el nombre del estudiante y su nota ")
    print("2 Opción calcular la media ")
    print("3 Opción mostar mejor estudiante ")
    print("4 Opción mostrar todos los estudiantes y sus notas ")
    print("5 Opción finalizar el programa ")
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")


    opcion=str(input("Ingrese el numero del menu según su opción: "))
    print("----------------------------------------------")

    match opcion: #menu

        case "1":
            print("Pautas a seguir primero se ingresa el nombre del estudiante y posteriormente se le solicitara la nota")
            print("-")
            nombre=str(input("1º Ingrese el nombre del estudiante: "))
            nota=float(input("2º Ingrese la nota del estudiante: "))
            print("-")
        case "2":
            #notamedia =
            print("-")
        case "3":
            #mejor_estudiante =
            print("-")
        case "4":
            #estudiantes_notas =
            print("-")
        case "5":
            print("Programa finalizado")
            print("===================")
            break
        case _:
            print("Vuleva selecionar una opcón y asegurse de escribirlo correctamente")
            print("------------------------------------------------------------------")