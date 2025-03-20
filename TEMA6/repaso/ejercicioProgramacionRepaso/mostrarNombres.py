import os
from Excepcion import FicheroNoEncontrado
def mostrarNombres():
    archivo="cine.txt"
    try:
        try:
            with open(archivo, "r") as arch:
                listaFichero=arch.readlines()
            # listavacia=[]
            # for i in listaFichero:
            #     listavacia.append(i.strip().split(" - ")[0])
            # return listavacia
            for i in listaFichero:
                listavacia=i.strip().split(" - ")[0]
                print(listavacia)
        except FileNotFoundError:
            raise FicheroNoEncontrado
    except FicheroNoEncontrado as e:
        print(f"Error: {e}")