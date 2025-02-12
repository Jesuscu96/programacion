from Bomberos import Bombero
bomberos = []

while True:
    print("\n--- MENÚ BOMBEROS ---")
    print("1. Crear un nuevo bombero")
    print("2. Mostrar todos los bomberos")
    print("3. Modificar un bombero")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        edad = int(input("Edad: "))
        especialista = input("¿Es especialista? (s/n): ").lower() == "s"
        nuevo_bombero = Bombero(nombre, apellidos, edad, especialista)
        bomberos.append(nuevo_bombero)
        print("Bombero creado con éxito.")
    elif opcion == "2":
        if not bomberos:
            print("No hay bomberos registrados.")
        else:
            for bombero in bomberos:
                print(bombero.mostrar_informacion())
                
    elif opcion == "3":
        if not bomberos:
            print("No hay bomberos registrados.")
        else:
            i=1
            for bombero in bomberos:
                print(f"{i} - {bombero.mostrar_informacion()}")
                i+=1
            seleccion = int(input("Selecciona el número del bombero a modificar: ")) - 1
            if 0 <= seleccion < len(bomberos):
                bombero = bomberos[seleccion]
                print("Deja el campo vacío si no quieres modificarlo.")
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_apellidos = input("Nuevos apellidos: ")
                nueva_edad = input("Nueva edad: ")
                nuevo_especialista = input("¿Es especialista? (s/n): ")
                
                if nuevo_nombre:
                    bombero.set_nombre(nuevo_nombre)
                if nuevo_apellidos:
                    bombero.set_apellidos(nuevo_apellidos)
                if nueva_edad:
                    bombero.set_edad(int(nueva_edad))
                if nuevo_especialista:
                    bombero.set_especialista(nuevo_especialista.lower() == "s")
                    
                print("Bombero modificado con éxito.")
            else:
                print("Selección no válida.")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")