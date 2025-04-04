import os
import shutil
from datetime import datetime


class MiExcepcionFichero(Exception):
    def __init__(self, mensaje="Error al crear fichero"):
        super().__init__(mensaje)
class MiExcepcionDirectorio(Exception):
    def __init__(self, mensaje="Error del Directorio"):
        super().__init__(mensaje)
class FechaErronea(Exception):
    def __init__(self, mensaje="Error de formato de fecha"):
        super().__init__(*mensaje)
listaErrores = []
try:    
            
    def CrearDirectorio(fechaformateada):
        carpeta = input("Ingrese el nombre del directorio: ")
        try:
            if not os.path.exists(carpeta):
                os.mkdir(carpeta)
                print(f"Se ha creado el directorio {carpeta}")
            else:
                print("Ya existe el directorio")
        except Exception as e:
            listaErrores.append(MiExcepcionDirectorio(f"Error con la creación del directorio: {e}"))
        
        # Ruta completa del fichero
        rutafichero = os.path.join(carpeta, "texto.txt")
        usuario = input("Introduce el nombre de usuario: ")
        
        try:
            with open(rutafichero, "a+", encoding="utf8") as archivo:
                archivo.write(f"{usuario} - {fechaformateada}\n")
            print("Registro creado")
        except Exception as e:
            listaErrores.append(MiExcepcionFichero(f"Error en la escritura o lectura del fichero: {e}"))
            
    try:
        def registrarFecha():
            fecha= input("Introduce la fecha de devolucion en esete formaro dd-mm-YYYY: ")
            fechaFormateada = datetime.strptime(fecha, "%d-%m-%Y")
            print("fecha registrada")
            
                
    except ValueError as e:
        
        listaErrores.append(FechaErronea("Error de formato de la fecha"))
        
    
    def borrarDirectorio():
        carpeta = input("Introduce en nombre de la carpeta que deseas borrar: ")
        try:
            if os.path.exists(carpeta):
                shutil.rmtree(carpeta)
                print("Borrado completado")
            else:
                print("La carpeta no existe")
        except Exception as e:
            listaErrores.append(MiExcepcionDirectorio("Error con la eliminación del directorio"))
        
                
    
    
   
           
    
except Exception as e:
    print ("Hubo un error en el codigo")
#
registrarFecha()
CrearDirectorio()
borrarDirectorio()