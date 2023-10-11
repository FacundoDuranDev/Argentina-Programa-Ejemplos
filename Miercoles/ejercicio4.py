# Desarrolle un programa que lea el archivo random_passwords.txt 
# generado en el ejercicio anterior y devuelva un diccionario con
# la cantidad de caracteres distintos que se encuentran en el archivo leído
# por ejemplo, si encuentra 5 letras “a” minuscula debe escribir a 5.
import string
with open(
    "C:\\Users\\nubim\\Desktop\\Argentina Programa\\random_pass.txt"
          ) as archivo:
    texto_total = str(archivo.read())
    lista_contraseñas = texto_total.split("\n")
    caracteres = string.ascii_letters + string.digits + string.punctuation
    diccionario = {
        letra : 0 for letra in caracteres
    }
    for contraseña in lista_contraseñas:
        for caracter in contraseña:
            if caracter in list(diccionario.keys()):
                diccionario[caracter] = diccionario[caracter] + 1
    print(diccionario)