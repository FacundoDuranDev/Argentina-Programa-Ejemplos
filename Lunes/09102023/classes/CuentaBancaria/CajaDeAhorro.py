from classes.CuentaBancaria.CuentaBancaria import CuentaBancaria
# Subclase CajaDeAhorro, modifica el método retirar para que,
# si el retiro supera el saldo, se muestre un mensaje de advertencia
#  y no se permita el retiro.

class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nombre_cuenta, saldo):
        super().__init__(nombre_cuenta, saldo)
    
    def retirar(self, monto):
        if self.saldo - monto < 0:
            print("estás intentando retirar más dinero del disponible en tu cuenta")
        else:
            self.saldo -= monto
            print(f"retiraste {monto}")