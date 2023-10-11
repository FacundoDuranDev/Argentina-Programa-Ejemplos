# Utilizando el módulo datetime desarrolle un programa que lea por
# teclado una fecha de cumpleaños con el formato dd/mm/aaaa e imprima
# cuanto tiempo falta para el siguiente cumpleaños en esa fecha.
from datetime import datetime

hoy = datetime.now().date()
input_string = input("Añada su fecha de cumpleaños en formato dd/mm/yyyy") 
#=> formato dia mes año "dd/mm/aaaa"
#=> Zonas horarias Greenwitch Meridian Time => GMT Argentina -3 
#=> Universal Time Coordinated => UTC Argentina -3
fecha_cumpleaños = datetime.strptime(input_string, "%d/%m/%Y")
proximo_cumpleaños = fecha_cumpleaños.replace(year=hoy.year).date()
if proximo_cumpleaños < hoy:
    proximo_cumpleaños = proximo_cumpleaños.replace(year=hoy.year + 1)

diferencia = proximo_cumpleaños - hoy
print(f"faltan {diferencia.days} días para tu cumpleaños")
print("Breakpoint final")