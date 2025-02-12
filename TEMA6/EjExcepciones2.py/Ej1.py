# Ejercicio 1: Crea un programa para pedir por teclado el nombre al usuario, y a continuación solicitar 10
# puntuaciones de supuestos exámenes, para después hacer una media para mostrarla por pantalla.
# Crea un método que pida los datos por pantalla realizando un control de errores que haga que si no
# se han introducido datos válidos en las notas, muestre un mensaje por pantalla.
# Las notas se guardarán en una lista.
nota = []
class Examanes:
    def pedir(self):
            try:
                contador = 0
                while True:
                    if contador <= 9:
                        notas =  float(input("Introduzca la nota: "))
                        nota.append(notas)
                        contador += 1
                    else:
                        break
                    print(nota)
            except ValueError:
                print("Ingrese bien la nota no vale un str (texto) ")
                 
    def mostrar(self):
        media = sum(nota)/ len(nota)
        return print(f"Nota media: {media}")
 
nombre = str(input("Ingrese el nombre de ususario: "))
while True:

        print("Op.1 Ingresar 10 notas de examenes ")
        print("Op.2 Hacer media de la nota y  mostrar por pantalla ")
        print("Op.3 Fin del programa")
        #nombre = str(input("Ingrese el nombre de ususario: "))
        op = int(input("Ingrese la opción que desee (1, 2 o 3): "))
        match op:
            case 1:
                Examanes.pedir()
            case 2:
                Examanes.mostrar()
            case 3:
                print("Fin del programa")
                break
            case _:
                print("Ingrese bien los numeros. ")
            
            