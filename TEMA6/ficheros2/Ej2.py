while True:
    print("\n--- Menú de combate ---")
    print("1. Introduce un nuevo contacto.")
    print("2. Buscar por nombre.")
    print("3. Mostrar datos.")
    print("4. Guadar en fichiero.")
    print("5. borrar contacto.")
    print("6. Salir.")
    
    
    Ej2= open("agenda.txt","r+" ,encoding = "utf-8")
   
    try:
        opcion = input("Elige una opción: ")
        
        match opcion:
            case "1":
                for i in range (20):            
                    nombre = str(input("Introduce un nombre: "))
                    tlf = int(input("Introduce el numero de teléfono: "))
                
                Ej2.write(f"Nombre: {nombre} , Numero de teléfono: {tlf}. \n")
            case "3":
                if Ej2:
                    print("Mostrar datos: ")
                    print(Ej2.read())
            case "4:
                
            case "5:"
            case "6":
                print("Fin del programa")
                Ej2.close()
                break
            case _:
                print("introduce de nuevo la opciones que son 1, ... o 6.")
        
        
    except ValueError:
        print("Has introducido un tipo str en un int")
    except FileNotFoundError:
        print("El archivo no existe.")
    finally:
        Ej2.close()