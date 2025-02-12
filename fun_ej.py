lista=[]

def agregar(lista):
    while True:
        x = int(input("Introduzca 1 si quiere agregar un nombre a la listo si no un 2: "))
        if x==1:
            nombre=str(input("Introduce el nombre aadel estudiante: "))
            lista.append(nombre)
        else:
            break
def eleminar(lista):
    nombre=str(input("Introduce el nombre del estudiante a borrar: "))
    lista.remove(nombre)
def mostrar(lista):
    print(lista)


agregar(lista)
eleminar(lista)
mostrar(lista)