try:
        Ej3 = open("datos_2.txt","r+")
        while True:
            print("\n--- Menú de combate ---")
            print("1. introduce un nombre y edad")
            print("2. Salir")

            opcion = input("Elige una opción: ")
            
            match opcion:
                case "1":            
                    nombre = str(input("introduce un nombre: "))
                    edad = int(input("introduce la edad: "))
                case "2":
                    print("Fin del programa")
                    Ej2.close
                    break
                case _:
                    print("introduce de nuevo la opciones que son 1 o 2.")
        
            Ej3.write(f"nombre: {nombre}, edad: {edad}. \n")
except ValueError:
    print("Error al introducir un str en un int")
finally:
    Ej3.close()
    print("Se cerró el archivo.")