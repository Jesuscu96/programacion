class CuentaBancaria:
    saldo_total = 0
    def __init__(self, numero_cuenta=0, titular="Sin titular", saldo=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo
        CuentaBancaria.saldo_total += saldo
   
    def ingresar(self, cantidad):
        self.saldo += cantidad
        CuentaBancaria.saldo_total += cantidad
   
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            CuentaBancaria.saldo_total -= cantidad
        else:
            print(f"No hay saldo suficiente en la cuenta {self.numero_cuenta} para retirar {cantidad}.")
