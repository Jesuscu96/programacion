import os

def borrar():
    try:
        archivo="cine.txt"

        if not os.path.exists(archivo):
            print("No existen registros.")
            return
        
        with open(archivo,"r") as arch:
            listaConNombresYFechas=arch.readlines()
            

       
        for u in listaConNombresYFechas:
            print(u.strip().split(" - ")[0])
            
        nombre = str(input("Dime el nombre a borrar"))
        for i in listaConNombresYFechas:
            if nombre in i:
                listaConNombresYFechas.remove(i)
                for i in listaConNombresYFechas:
                    with open(archivo, "w") as arch:
                        arch.write(i)
                        print(f"registro borrado")
            
            
    except Exception as e:
        print(f"ha Ocorrido un error en el intento de borrar {e}")        
    


borrar()