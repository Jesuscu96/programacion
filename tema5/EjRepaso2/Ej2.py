class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidadD):
       return cantidadD = float(input("Ingresa una catidad de saldo: "))

    def retirar(self, cantidadR):
        return cantiadadR = float(input("Retira una catidad de saldo: "))
    
    def mostrar(self):
        return f"El titula es {self.titular} y saldo es de {self.saldo} €."
    
    def __add__(self, objeto2):
        s = self.saldo+objeto2.saldo
        return s
    
while True:

    print("Op.1 Crear cuanta con titular y saldo.")
    print("Op.2 Depositar cantidad en saldo.")
    print("Op.3 Retirar cantidad en saldo.")

