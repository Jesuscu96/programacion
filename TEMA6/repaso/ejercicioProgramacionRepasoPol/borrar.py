import os
def borrar():
    archivo="cine.txt"

    if not os.path.exists(archivo):
        print("No existen registros.")
        return
    
    with open(archivo,"r") as arch:
        listaConNombresYFechas=arch.readlines()
        for i in listaConNombresYFechas:
            print(i.strip().split(" - ")[0])

    # print(listaConNombresYFechas)
    nombreborrar=input("Dime el nombre del cinefilo a borrar: ")
    for i in listaConNombresYFechas:
        if nombreborrar in i:
            listaConNombresYFechas.remove(i)
            with open(archivo,"w") as arch:
                for i in listaConNombresYFechas:
                    arch.write(i)
                    print("Cinefilo borrado con exito")


    


# borrar()