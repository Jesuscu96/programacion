class Biblioteca:    
    from Libros import Libro
    libros = []

    while True: # Menu
        print("\n--- MENÚ Libreria ---")
        print("1. Añadir un nuevo libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Consultar informacón del libro")
        print("5. Indicar cuantos libros tiene la biblioteca y mostrar todos los titulos")
        print("6. Finalizar el programa")
        opcion = str(input("Selecciona una opción entre el 1 y el 6: "))
        match opcion:
            case "1": # Añadir un libro
                print("Introduzca los datos necesarios para añadir el libro. ")
                titulo = input("Introduce el titulo: ")
                autor = input("Introduce el autor: ")
                isbn = int(input("Introduce el isbn: "))
                prestado = input("¿Esta prestado? (s/n): ").lower() == "s"

                nuevo_libro = Libro(titulo, autor, isbn, prestado)
                libros.append(nuevo_libro)
                print("Datos del libro añadidos con exito.")
            case "2": # Prestar un libro
                if 
            case "3": # Devolver un libro
                if
            case "4":# Mostrar la información
                if not libros:
                    print("No hay libros registrados.")
                else:
                    for libro in libros:
                        print(libros.mostrar_informacion())
            
            case "5": # Indicar la cantidad de libros y mostrar los titulos
            
            case "6": # Finalizar el programa
                print("El programa se ha finalizado.")
                break
            case _: # Error al introducir los numeros
                print("Introduza correctamente los nuemros entre el 1 y el 6")