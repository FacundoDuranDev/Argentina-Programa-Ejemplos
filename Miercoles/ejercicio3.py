# Desarrolle un programa que reciba por parámetro del script
# un número entero y escriba en un archivo llamado random_passwords.txt
# una cantidad igual al número pasado por parámetro de strings de longitud
# igual a 16 que incluyan letras minúsculas, mayúsculas, números y 
# caracteres especiales aleatorios.
import random
import string
import sys
#=> "sys" es uno de los modulos mas importantes
# porque nos permite interactuar con el sistema (System)
# también está el modulo "os" que es para interactuar con
# el sistema operativo (apagar la pc, prenderla, etc...)
def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for number in range(longitud))
    return contraseña

def escribir_archivo(nombre_archivo, cantidad):
    with open(nombre_archivo, "w+") as archivo: #=> write file
        for number in range(cantidad):
            contraseña = generar_contraseña(16)
            archivo.write(contraseña + "\n")

if __name__ == "__main__": 
    #=> siempre y cuando nuestro archivo esté siendo ejecutado directamente desde
    # este archivo, va a ejecutar el codigo, de otra manera, en caso de que 
    # estemos importando de este archivo por ejemplo, una función, no se va
    # a ejecutar esta condición.
    if len(sys.argv) != 2:
        print("Uso: python ejercicio3.py <cantidad>")
        sys.exit(1)
    try:
        cantidad = int(sys.argv[1])
    except ValueError:
        print("ingresa un numero válido")
        sys.exit(1)
    escribir_archivo("./random_pass.txt", cantidad)
    print("finalizado el proceso")