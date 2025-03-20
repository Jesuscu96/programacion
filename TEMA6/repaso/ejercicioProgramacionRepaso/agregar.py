from Excepcion import NombreEncontrado,DiaPosterior
from datetime import datetime

def agregarUsuario():
    archivo="cine.txt"
    
    try:
        try:
            with open(archivo, "r") as arch:
                fichero=arch.readlines()
        except FileNotFoundError:
            print("El archivo no existe. Te lo creo...")
            fichero=[]
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            
        nombre=input("Dime el nombre del cinéfilo: ")
        lista=[]
        for i in fichero:
            lista.append(i.strip().split(" - ")[0])
        if nombre in lista:
            raise NombreEncontrado()
        
        fecha=input(f"¿Cuándo vio la peli? (dd-mm-yyyy hh:mm:ss):  ")
        fechaformateada=datetime.strptime(fecha, "%d-%m-%Y %H:%M:%S")
        fechahoy=datetime.now()
        try:
            if fechahoy < fechaformateada:
                raise DiaPosterior()
            else:
                with open(archivo, "a") as arch:
                    arch.write(f"{nombre} - {fechaformateada}\n")
        except ValueError:
            print("Fecha incorrecta")
        print("Cinéfilo agregado con éxito")

    except NombreEncontrado as n:
        print(f"Ha ocurrido un error: {n}")
    except DiaPosterior as o:
        print(f"Ha ocurrido un error: {o}")