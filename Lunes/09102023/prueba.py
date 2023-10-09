import string
with open("C:\\Users\\nubim\\Desktop\Argentina Programa\Lunes\\09102023\\random_pass.txt", "r") as archivo_texto:
    texto_total = str(archivo_texto.read())
    lista_contraseñas = texto_total.split("\n")
    caracteres = string.ascii_letters + string.digits + string.punctuation
    diccionario = {letra: 0 for letra in caracteres}
    for contraseña in lista_contraseñas:
        for caracter in contraseña:
            if caracter in list(diccionario.keys()):
                diccionario[caracter] = diccionario[caracter] + 1
    print(diccionario)