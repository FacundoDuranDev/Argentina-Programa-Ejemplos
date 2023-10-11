from classes.CuentaBancaria.CuentaBancaria import CuentaBancaria
#Subclase CuentaCorriente:
# atributo adicional sobregiro que represente el límite de sobregiro
# permitido. Modifica el método retirar para que, si el retiro supera el 
# saldo y no excede el límite de sobregiro, se permita el retiro
# y se actualice el saldo. Si el retiro supera el límite de sobregiro, 
# se debe mostrar un mensaje de advertencia.

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_cuenta, saldo, sobregiro):
        super().__init__(nombre_cuenta, saldo)
        self.sobregiro = sobregiro

    def retirar(self, monto):
        if self.saldo <= 0:
            if self.sobregiro > 0 and self.sobregiro - monto >= 0:
                self.sobregiro -= monto
                print(f"retiraste {monto} de tu sobregiro")
            else:
                print("excediste tu limite de sobregiro")
        else:
            self.saldo -= monto
            print(f"retiraste {monto}, tu sobregiro total es {self.sobregiro}")
    
