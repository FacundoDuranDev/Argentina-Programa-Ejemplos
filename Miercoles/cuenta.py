from classes.CuentaBancaria.CuentaBancaria import CuentaBancaria
from classes.CuentaBancaria.CuentaCorriente import CuentaCorriente
from classes.CuentaBancaria.CajaDeAhorro import CajaDeAhorro
#from directorio.directorio.archivo import nombreClase

cuenta_1 = CuentaBancaria("Facundo", 2000)
cuenta_1.retirar(100)
cuenta_1.depositar(50)
print(cuenta_1.obtener_saldo())
cuenta_corriente_1 = CuentaCorriente("Horacio",2000,1000)
cuenta_corriente_1.retirar(2000)
print(cuenta_corriente_1.obtener_saldo())
cuenta_corriente_1.retirar(1000)
print(cuenta_corriente_1.obtener_saldo())
print(cuenta_corriente_1.obtener_saldo())
caja_de_ahorro = CajaDeAhorro("Brenda", 2000)
caja_de_ahorro.retirar(2001)
print(caja_de_ahorro.obtener_saldo())