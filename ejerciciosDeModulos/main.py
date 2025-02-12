'''Ejercicio 1: Gestión de productos de una tienda:
    Crea un módulo productos.py que tenga las siguientes funciones:
        • agregar_producto(lista, producto): Agrega un producto (como string) a la lista de productos.
        • eliminar_producto(lista, producto): Elimina un producto de la lista si existe.
        • mostrar_productos(lista): Muestra todos los productos en la lista.

    Crea otro módulo main.py que importe el módulo anterior y:
        • Inicialice una lista vacía para los productos.
        • Permita al usuario interactuar mediante un menú: agregar, eliminar o listar productos, o salir.'''


main = __name__
lista = []
import productos

while True:
    print("   Agrega un producto a la lista ingrese el numero 1")
    print("   Eleminar un producto de la lista ingrese el numero 2")
    print("   Mostrar el numero de la lista ingrese el numero 3")
    print("   Si desea fianalizar el programa ingrese el numero 4")
    print("----------------------------------------------------------")
    print("----------------------------------------------------------")
    opcion1=str(input("ingrese un numero según a opción que desee: "))
    
    match opcion1:
        case "1":
           producto_agregar =str(input("introduce un producto: "))
           productos.agregar(lista, producto_agregar)
           
        case "2":
            producto_eleminar = input("¿Qué producto deseas eliminar? ")
            productos.eleminar(lista, producto_eleminar)
        
        case "3":
            
            productos.mostrar(lista)

        case "4":
            print("fin del programa")
            break

        case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

