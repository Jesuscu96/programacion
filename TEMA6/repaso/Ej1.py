from datetime import datetime
import os

class  FechapasadaError(Exception):
    def __init__(self, mensaje="fecha pasado de plazo"):
        super().__init__(mensaje) = mensaje
        
        

def registrar():
    try:
        try:
            archivoAsistentes = "asistencia.txt"
            listanombres= []
            with open(archivoAsistentes, "r") as archivo:
                for linea in archivo:
                    listanombres.append(linea.strip().split()[0])
        except FileNotFoundError:
            pass
          
        
        nombres = input(str("Introduce un nombre: "))
        
        for nombre in  nombres:
            if nombre not in listanombres:
                listanombres.append(nombres)
                fechainscripcion = datetime.now().strftime("%d-%m-%Y")
            else:
                print("ya se ha registrado tu asistencia.")
                return
            with open(archivoAsistentes, "a"):
                archivoAsistentes.write(f"{nombre} - {fechainscripcion}")
            print("Registrado")
    except Exception as e:
        print(f"Se ha cometido un error {e}")

registrar()