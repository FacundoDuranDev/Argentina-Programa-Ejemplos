# Desarrolle un programa que reciba por parámetro del script
# un número entero y escriba en un archivo llamado random_passwords.txt
# una cantidad igual al número pasado por parámetro de strings de longitud
# igual a 16 que incluyan letras minúsculas, mayúsculas, números y 
# caracteres especiales aleatorios.
import random
import string
import sys 
#=> es uno de los modulos mas importantes
# porque nos permite gestionar nuestro sistema

def generar_contraseña(longitud):
    caracteres = string.ascii_letters +string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for number in range(longitud))
    return contraseña

def escribir_archivo(nombre_archivo, cantidad):
    with open(nombre_archivo, "a+") as archivo: #=> write)
        for number in range(cantidad):
            contraseña = generar_contraseña(16)
            archivo.write(contraseña + "\n")

if __name__ == "__main__": 
    #=> siempre y cuando nuestro archivo esté siendo ejecutado desde este archivo, va a 
    # ejecutar el codigo, de otra manera, en caso de que estemos importando por ejemplo
    # una función, no se va a ejecutar este pedazo de codigo lo cual es importante porque
    # define el comportamiento de nuestro paquete (Package)
    if len(sys.argv) != 2:
        print("Uso: python ejercicio3.py <cantidad>")
        sys.exit(1)
    try:
        cantidad = int(sys.argv[1])
    except ValueError:
        print("ingrese un numero valido")
        sys.exit(1)
    if cantidad <= 0:
        print("la cantidad debe ser un numero entero positivo")
        sys.exit(1)
    escribir_archivo("random_pass.txt", cantidad)