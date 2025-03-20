
import os
import shutil
from datetime import datetime
'''
def crear_directorio(dir,nom):
    directorio_dir = os.path.join(dir, nom)
    if not os.path.exists(directorio_dir):
        os.makedirs(directorio_dir)
    else:
        print("El directorio ya existe.")

    
def crear_fichero(dir, nom):
    rutaFichero = os.path.join(dir, nom )
    fecha_str = input("introduce una fecha segun este formato dd-mm-yyyy: ")
    fecha_formateada = datetime.strptime(fecha_str, "%d-%m-%Y")
    dir = input("introduce el nombre del usuario: ")
    with open (os.path.join("ficheros.txt"),"a", encoding = "utf-8") as fichero:
        fichero.write(f"{nom} - {fecha_formateada} \n")
        


    
while True:
    print("1 crear usuario y escribirlo en el fichero.")
    print("2 salir")
    op = input("introduce la opcion que deseas: ")
    match op:
        case "1":
            crear_directorio(dir)
            crear_fichero(dir)
        case "2":
            break
        case _:
            print("vuelve a introducir una opción")'''

class Error_Fichero(Exception):
    def __init__(self, mensaje="Error al crear fichero"):
        super().__init__(mensaje)            
            
def crear_carpeta(usuario):
    if not os.path.exists(usuario):
        os.makedirs(usuario)
        print(f"La carpeta con el nombre {usuario} se ha creado.")
    else:
        print(f"La carpeta {usuario} ya existe")

def crear_archivo_texto(usuario):
    rutaFichero= os.path.join(usuario, "fichero.txt")
    fecha_str = input("introduce la fecha con este formato, dd-mm-yyyy: ")
    
    try:
        fechaformateada = datetime.strptime(fecha_str, "%d-%m-%Y")
        #if os.path.exists("fichero.txt"):
        with open(rutaFichero, "w", encoding="utf8") as fichero:
            fichero.write(f"{usuario} - {fechaformateada} \n")
        print("Fichero creado con exito.")
        
                
    except ValueError:
        print("Formato de fecha incorrecto")    
    except Exception as e:
        raise Error_Fichero()
    
def borrar_carpeta(usuario):
    if os.path.exists(usuario):
        shutil.rmtree(usuario)
        print("Directorio borrado con exito.")
    else:
        print("El directorio introducido no existe. \n Recomiendo que compruebe si lo escribio bien.")
        

while True:
    print("1. Crear usuario y escribirlo en el fichero.")
    print("2. Borrar usuario. ")
    print("3. salir")
    op = input("introduce la opcion que deseas: ")
    match op:
        case "1":
            usuario = input("introduce el nombre de usuario: ")
            crear_carpeta(usuario)
            
            crear_archivo_texto(usuario)
        case "2":
            usuario = input("introduce el usuario a borrar: ")
            borrar_carpeta(usuario)
        case "3":
            break
        case _:
            print("vuelve a introducir una opción")
