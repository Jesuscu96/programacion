from cliente import Cliente

if __name__ == "__main__":
    cliente_1 = Cliente(1, "juan", "Perez Goñi", "Oro")
    cliente_2 = Cliente(2, "Luis", "Soriano Garcia", "Plata")
    cliente_3 = Cliente(3, "Faustino", "Perez Perez", "")
    

   
    print(f"{cliente_1.nombre_cliente()}: {cliente_1.muestra_datos()}")
    print(f"{cliente_2.nombre_cliente()}: {cliente_2.muestra_datos()}")
    print(f"{cliente_3.nombre_cliente()}: {cliente_3.muestra_datos()}")

    print(f"Total de clientes: {Cliente.total_clientes_actual()}")
    


        