#Clase (base) CuentaBancaria:
#- Atributos:
#	- nombre_cuenta
#	- saldo.
#- Métodos:
#- Método constructor con todos los atributos pasados por parámetro.
#	- depositar: dado un número pasado por parámetro suma el número al saldo actual de la cuenta.
#	- retirar:  dado un número pasado por parámetro resta el número al saldo actual de la cuenta.
#	- obtener_saldo: retorna el saldo actual de la cuenta.

class CuentaBancaria:
    def __init__(self, nombre_cuenta, saldo):
        self.nombre = nombre_cuenta
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"depositaste {monto}")
    
    def retirar(self, monto):
        self.saldo -= monto
        print(f"retiraste {monto}")
    def obtener_saldo(self):
        return self.saldo