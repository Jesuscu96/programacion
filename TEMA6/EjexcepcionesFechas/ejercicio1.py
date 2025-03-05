from datetime import datetime

class Miexcepcion(Exception="Este es mi error"):
    def __init__(self, mensaje):
        self.mensaje = mensaje


def gestionar():
    try:
        nombre = input("Indica tu nombre: ")
        fechatexto = input("Indica la fecha de la cita (DD-MM-YYYY): ")
        fecha = datetime.strp(fechatexto,"%d-%m-%Y" )
        fechahoy=datetime.now()
        if fecha < fechahoy:
            raise Miexcepcion ("Error: fecha anterior a hoy")
        with open('citas.txt','a') as fichero:
            fichero.write(f"{nombre} - {fechatexto}\n")


    except ValueError:
        print("fecha incorrecta")

    except Miexcepcion as e:
        print(e.mensaje)

    except OSError:
        print("Errores de fichero")
    except Exception:
        print("ERROR GLOBAL")

gestionar()