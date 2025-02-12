from partA import CuentaBancaria
cuenta1 = CuentaBancaria(1, "Juan Perez", 0)
cuenta2 = CuentaBancaria(2, "Luis Soriano", 100)
cuenta3 = CuentaBancaria(3, "Faustino Perez", 5000)
cuenta1.ingresar(200)
cuenta2.ingresar(100)
cuenta3.retirar(300)
cuenta1.ingresar(1000)
print(f"{cuenta1.titular}: {cuenta1.saldo}")
print(f"{cuenta2.titular}: {cuenta2.saldo}")
print(f"{cuenta3.titular}: {cuenta3.saldo}")
print(f"Saldo total de todas las cuentas: {CuentaBancaria.saldo_total}")


