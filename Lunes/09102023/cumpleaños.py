# Utilizando el módulo datetime desarrolle un programa que lea por teclado
# una fecha de cumpleaños con el formato (dd/mm/aaaa) e imprima cuanto tiempo
# falta para el siguiente cumpleaños en esa fecha.
from datetime import datetime
fecha_cumpleaños = datetime.strptime("28/05/1999", "%d/%m/%Y")
fecha_actual = datetime.now()
# fecha_cumpleaños = input("ingresa tu fecha de cumpleaños en formato dd/mm/yyyy")
hoy = fecha_actual.date()
proximo_cumpleaños = fecha_cumpleaños.replace(year=hoy.year).date()
if proximo_cumpleaños < hoy:
    proximo_cumpleaños = proximo_cumpleaños.replace(year=hoy.year + 1)

diferencia = proximo_cumpleaños - hoy
print(f"Faltan {diferencia.days} días para su proximo cumpleaños")