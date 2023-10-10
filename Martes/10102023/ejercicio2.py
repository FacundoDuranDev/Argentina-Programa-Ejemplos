# Utilizando el módulo datetime desarrolle un programa que lea por
# teclado una fecha de cumpleaños con el formato dd/mm/aaaa e imprima
# cuanto tiempo falta para el siguiente cumpleaños en esa fecha.
from datetime import datetime

hoy = datetime.now().date()
fecha_string = input("Añada su fecha de cumpleaños en el formato dd/mm/yyyy")
fecha_cumpleaños = datetime.strptime(fecha_string, "%d/%m/%Y")
proximo_cumpleaños = fecha_cumpleaños.replace(year=hoy.year).date()
if proximo_cumpleaños < hoy:
    proximo_cumpleaños = proximo_cumpleaños.replace(year= hoy.year + 1)

diferencia = proximo_cumpleaños - hoy
print(f"Faltan {diferencia.days} días para tu cumpleaños")