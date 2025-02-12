from producto import Productos

if __name__ == "__main__":
    producto_1 = Productos(1, "Cascos", 60)
    producto_2 = Productos(2, "Raton y teclado", 80)
    producto_3 = Productos(3, "Monitor", 210)
    

   
    print(f"{producto_1.muestra_datos()}")
    print(f"{producto_2.muestra_datos()}")
    print(f"{producto_3.muestra_datos()}")

    print(f"Total de poductos es: {Productos.total_productos()}")
    


        