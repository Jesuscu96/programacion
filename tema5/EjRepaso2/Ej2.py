class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidadD):
        self.saldo += cantidadD
        return self.saldo
    def retirar(self, cantidadR):
        if cantidadR > self.saldo:
            print("Saldo insuficiente.")
        elif cantidadR < 0:
            print("La cantidad a retirar debe ser positiva.")
        else:
            self.saldo -= cantidadR        
        return self.saldo
    def mostrar(self):
        return f"El titular es {self.titular} y saldo es de {self.saldo} €."
    
    def __add__(self,objeto1):
        s1 = self.saldo+objeto1.saldo
        return s1
    
    '''def __sub__(self, objeto1):
        s2 = self.saldo-objeto1.saldo       
        return s2'''
obj1 = CuentaBancaria("Jose", 2400)
obj2 = CuentaBancaria("Luis", 3200)


while True:

    #print("Op.1 Crear cuanta con titular y saldo.")
    print("Op.1 Depositar cantidad en saldo.")
    print("Op.2 Retirar cantidad en saldo.")
    print("Op.3 Imprime el saldo de ambas cuentas antes y después de las transacciones.")
    print("Op.4 Fin del programa")

    op = int(input("Introduce la opción: "))

    match op:
        
        case 1:
            cantidadD = float(input("Ingresa una catidad de saldo: "))
            obj1.depositar(cantidadD)
            cantidadD = float(input("Ingresa una catidad de saldo: "))
            obj2.depositar(cantidadD)
            #cantidadD = float(input("Ingresa una catidad de saldo: "))
        case 2:
            cantidadR = float(input("Retira una catidad de saldo: "))
            obj1.retirar(cantidadR)
            cantidadR = float(input("Retira una catidad de saldo: "))
            obj2.retirar(cantidadR)
            
        case 3:
            print("--Antes de la transación--")
            print(obj1.mostrar())
            print(obj2.mostrar())
            print("--Despues de la transación--")
            print(obj1 + obj2)
        case 4:
            print("Fin del programa")
            break
        case _:
            print("Opcion no valida o incorrecta.")