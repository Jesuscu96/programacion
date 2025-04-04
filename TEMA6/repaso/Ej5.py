import os
import shutil
from datetime import datetime

def CrearDirectorio():
    carpeta = input("Ingrese el nombre del directorio Ej Pedro.txt: ")
    if not os.path.exists(carpeta):
        os.mkdir(carpeta)
        print(f"Se ha creado el directorio {carpeta}")
    else:
        print("Ya existe el Directorio")
CrearDirectorio()