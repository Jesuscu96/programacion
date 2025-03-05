import os 
import webbrowser

dir_home = os.path.dirname(__file__)

for archivo in os.listdir(dir_home):
    print(archivo)

archivo_abrir = input("Escriba el archivo que desee abrir: ")

if archivo_abrir in os.listdir(dir_home):
    webbrowser.open(dir_home + "/" + archivo_abrir)

else:
    print("El archivo no se ha encontrado")