# Desarrolle un programa que reciba por parámetro del script un número entero
# y escriba en un archivo llamado random_passwords.txt una cantidad igual al
# número pasado por parámetro de strings de longitud igual a 16 que incluyan 
# letras minúsculas, mayúsculas, números y caracteres especiales aleatorios.
import random
import string
import sys
# sys es una de las liberías que nos permite interactuar con el sistema

def generar_password_aleatorias(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for number in range(longitud))
    return contraseña

def escribir_archivo(nombre_archivo, cantidad):
    with open(nombre_archivo, "w") as archivo:# write
        for number in range(cantidad):
            contraseña = generar_password_aleatorias(16)
            archivo.write(contraseña + "\n")

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Uso: python random_generator.py <cantidad>")
        sys.exit(1)
    try:
        cantidad = int(sys.argv[1])
    except ValueError:
        print("por favor, ingrese un numero válido")
        sys.exit(1)
    if cantidad <= 0:
        print("la cantidad debe ser un numero entero positivo")
        sys.exit()
    escribir_archivo("random_pass.txt",cantidad)
        