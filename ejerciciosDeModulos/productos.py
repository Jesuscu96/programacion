def agregar(lista, producto_agregar):
    
    #producto = str(input("introduce un producto: "))
    lista.append(producto_agregar)
    print("producto agreagado")
          
def eleminar(lista, producto_eleminar):
    
    #producto = input("¿Qué producto deseas eliminar? ")
    lista.remove(producto_eleminar)
    print("producto eleminado")

def mostrar(lista):
    
    print(f"Hay {len(lista)} productos en la lista.")
    print(lista)


lista=[]

