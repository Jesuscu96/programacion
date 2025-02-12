switch={}
# nombre=str(input("Introduce el nombre del juego: "))
# precios=int(input("Introduce el precio: "))
# cantidad=int(input("Introduce el stock: "))

dic=1
def agregar(switch):
    global dic
    
    nombre=str(input("Introduce el nombre del juego: "))
    precios=int(input("Introduce el precio: "))
    stock=int(input("Introduce el stock: "))
    switch[dic]={"nombre":nombre,"precio":precios, "stock":stock}
    dic+=1
    return "producto agregado con exito"

     

while True:
  print("1- introducir los datos de los productos")
  print("2- mostrar datos ")
  op=input(str("introduce la opción que deses realizar: "))
  match op:
    case "1":
      #cantidad=str(input("Cuantos juegos quiere introducir: "))
     # nombre=str(input("Introduce el nombre del juego: "))
      #precios=int(input("Introduce el precio: "))
      #stock=int(input("Introduce el stock: "))
      a=agregar(switch)
      
      print(a)
      
        
     
    case "2":
      print(switch)
    case "3":
      print("fin del programa")
      break
