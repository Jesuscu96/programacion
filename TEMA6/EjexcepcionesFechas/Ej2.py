'''from datetime import datetime 
import os
class Miexcepcion(Exception="Este es mi error"):
    def __init__(self, mensaje="Este es mi error"):
        self.mensaje = mensaje
def gestionar():
    try:
        listanombre = []
        asistentes = open("asistenetes.txt", "w+")
        while True:
            print("Op1: Introduce el nombre.")
            print("Op2: Finalizar el programa.")
            lineaAsistentes = asistentes.readline()
            
            
            op = int(input("Introduce una opción 1 o 2: "))
            match op:
                case 1:
                    nombre = str(input("Introduce un nombre: "))
                    for nombres in nombre:
                        if nombre not in listanombre:
                            listanombre.append(nombres)
                            fechainscrito = datetime.now()
                       
                            with open("asistentes.txt", "a+") as asistentesEscritura:
                                asistentesEscritura.write(f"{nombre} - {fechainscrito}\n")
                        else:
                            print("El nombre ya esta en la lista")
                        

                case 2: 
                    print("Fin del programa.")
                    break
                case _:
                    print("Ingrese bien las opciones 1 o 2.")
    except Miexcepcion:
    except ValueError:
        print("fecha incorrecta")

    except Miexcepcion as e:
        print(e.mensaje)

    except OSError:
        print("Errores de fichero")
    except Exception:
        print("ERROR GLOBAL") 
    except Miexcepcion:           

    
gestionar()'''

##################################################################################
from datetime import datetime
import os

class Miexcepcion(Exception):
    def __init__(self,mensaje="Error, fecha caducada"):
        self.__mensaje=mensaje
    
    #Crear el getter
    @property
    def mensaje(self):
         return self.__mensaje
    #Crear el setter
    @mensaje.setter
    def mensaje(self,valor):
         self.__mensaje=valor
"""

1. Primero ver si el archivo existe 
2. Si existe ver que hay dentro (recoger los nombres dentro del archivo y guardarlos dentro de una lista)
3. Si no existe: abrimos el archivo y recogemos los inputs, nombres a la lista y nombres y fecha al archivo.

"""
def registro():
    while True:
        fecha = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    #Comillas dobles porque estamos todos haciendo eso
    #y nos escribe el aÃ±o en dos dÃ­gitos

        try:
            print("MENU")
            print("1.AÃ±adir usuario")
            print("2.Salir")
            opcion = input("Dime que opcion quieres elegir: ")
            
            match opcion:
                case "1":

                    nombre = input("Dime un nombre a ingresar: ") 

                    with open("asistentes.txt", "a+") as asistentesLectura:
                        archivoleer = asistentesLectura.readlines()
                        for linea in archivoleer:
                            if nombre not in linea:
                                asistentesLectura.write(f"{nombre} ha sido creado a fecha {fecha}\n")
                            else:
                                print("El usuario ya existe")


                    
                            
                case "2":
                    print("Saliendo")
                    break
        except Miexcepcion as e:
            print(f"Error al abrir el archivo {e.mensaje}")


    registro()
    print("Hemos finalizado")