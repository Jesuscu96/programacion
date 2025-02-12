# Ejercicio 1: Crea un programa modular para convertir unidades de medida.
# Crea un paquete llamado conversores con los siguientes módulos:
# 
# longitud.py:
# Función metros_a_kilometros(metros): Convierte metros a kilómetros.
# Función kilometros_a_millas(kilometros): Convierte kilómetros a millas.
# 
# peso.py:
# Función kilogramos_a_libras(kg): Convierte kilogramos a libras.
# Función libras_a_kilogramos(libras): Convierte libras a kilogramos.
# 
# Crea un programa principal llamado conversor.py que:
# Importa las funciones necesarias del paquete.
# Permite al usuario seleccionar el tipo de conversión y proporciona los valores necesarios.
# Muestre el resultado de la conversión.
# Ejemplo de salida:
#
# 
# Selecciona una conversión:
# 1. Metros a kilómetros
# 2. Kilómetros a millas
# 3. Kilogramos a libras
# 4. Libras a kilogramos
# Tu elección: 2
# Introduce el valor en kilómetros: 5
# El resultado es: 3.107

conversor = __name__
from conversores import longitud
from conversores import peso


while True:
    print("-------------------------------")
    print("-------------------------------")
    print("1 opción de Metros a kilómetros")
    print("2 opción de Kilómetros a millas")
    print("3 opción de Kilogramos a libras")
    print("4 opción de Libras a kilogramos")
    print("5 opción fin del programa ")
    print("-------------------------------")
    print("-------------------------------")
    opcion=str(input("Selecciona la opción del menu según su numero: "))
    print("-------------------------------------------------")
    match opcion:
        case "1":
            metros=float(input("Ingrese los metros: "))
            print("-")
            kilometros=longitud.km(metros)
            print(" La totalidad de kilometros es", kilometros)

        case "2":
            kilometros=float(input("Ingrese los kilometros: "))
            print("-")
            millas=longitud.mill(kilometros)
            print("la totalidad de millas es",millas)
        case "3":
            kilogramos=float(input("Ingrese los kilogramos: "))
            print("-")
            libras=peso.kilo(kilogramos)
            print("La totalidad de libras es", libras)
        case "4":
            libras=float(input("Ingrese las libras: "))
            print("-")
            kilogramos=peso.lib(libras)
            print("La totalidad de kilogramos es",kilogramos)
        case "5":
            print("Fin del programa gracias")
            break
        case _:
            print("Vuelva a repetir la opcion que que desee")


