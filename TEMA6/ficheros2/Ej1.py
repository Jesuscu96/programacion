Ej1= open("Temperatura.txt","w" ,encoding = "utf-8")

while True:
    print("\n--- Menú de combate ---")
    print("1. Introduce nueva fecha (dd/mm/yyyy) con sus temperaturas.")
    print("2. Mostrar historial de registros.")
    print("3. Salir.")
    
    
    Ej1= open("Temperatura.txt","r+" ,encoding = "utf-8")
   
    try:
        opcion = input("Elige una opción: ")
        
        match opcion:
            case "1":            
                fecha = str(input("Introduce la fecha: "))
                tmax = int(input("Introduce la temperatura maxima: "))
                tmin = int(input("Introduce la temperatura minima: "))
                Ej1= open("Temperatura.txt","a" ,encoding = "utf-8")
                Ej1.write(f"Fecha: {fecha},\t Temperatura máxima: {tmax}ºc ,\t Temperatura mínima: {tmin}ºc. \n")
                
            case "2":
                if Ej1:
                    print("Mostrar registros: ")
                    print(Ej1.read())
                    temperaturaMax = 0
                    temperaturaMin = 0 
                    if temperaturaMax < tmax:
                        temperaturaMax = tmax
                    else: 
                        temperaturaMax = temperaturaMax
                    if temperaturaMin > tmin:
                        temperaturaMin = tmin 
                    else:
                        temperaturaMin = tmin
                    print(f"La temperatura mínima es de {temperaturaMin}ºc y la temperatura maxima es de {temperaturaMax}ºc")
            case "3":
                print("Fin del programa")
                Ej1.close()
                break
            case _:
                print("introduce de nuevo la opciones que son 1, 2 o 3.")
        
        
    
    except FileNotFoundError:
        print("El archivo no existe.")
    finally:
        Ej1.close()