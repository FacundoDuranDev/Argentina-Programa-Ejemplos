# Desarrolle un programa que lea el archivo random_passwords.txt 
# generado en el ejercicio anterior y escriba en un archivo llamado
# conteo.txt la cantidad de caracteres distintos que se encuentran en el archivo leído
# por ejemplo, si encuentra 5 letras “a” minuscula debe escribir a 5.
import string

with open(
    "C:\\Users\\nubim\\Desktop\Argentina Programa\Martes\\10102023\\random_pass.txt"
    ) as archivo_texto:
    texto_total = str(archivo_texto.read())
    lista_contraseñas = texto_total.split("\n")
    caracteres = string.ascii_letters +string.digits + string.punctuation
    diccionario = {
        letra: 0 for letra in caracteres
    }
    for contraseña in lista_contraseñas:
        for caracter in contraseña:
            if caracter in list(diccionario.keys()):
                diccionario[caracter] = diccionario[caracter] + 1
    print(diccionario)
