# Desarrolle un módulo/archivo para las clases Materia
# y Alumno desarrolladas en el punto II (uno para cada una)
# y luego desarrolle la clase Academia que importe ambas clases.
# La clase Academia debe contar con las siguientes funciones:
# Cantidad de alumnos aprobados por año:
#  retorna la cantidad de alumnos con todas las materias aprobadas de un año pasado por parámetro.
# Alumnos egresados: 
# retorna una lista de los alumnos que tienen todas las materias aprobadas.
from classes.Academia.Alumno import Alumno
from classes.Academia.Materia import Materia
from academia import lista_materias_1, lista_materias_2
# no tengo que copiarme el codigo directamente de chat gpt, tengo que testearlo
# no tengo que copiarme el codigo directamente de chat gpt, tengo que testearlo
# no tengo que copiarme el codigo directamente de chat gpt, tengo que testearlo
# no tengo que copiarme el codigo directamente de chat gpt, tengo que testearlo
class Academia:
    def __init__(self,nombre_academia, alumnos):
        self.nombre = nombre_academia
        self.alumnos = alumnos
    
    def alumnos_reprobados(self, año, aprueba_con):
        materias_reprobadas = list()
        alumnos_reprobados = list()
        # ctrl + k + c 
        # comentamos la selección que tengamos 
        # MUY UTIL
        # ctrl + d 
        # selección multiple
        # ctrl + k + u
        for alumno in self.alumnos:
            if alumno.materias_desaprobadas(aprueba_con):
                materias_reprobadas.append(alumno)
        for alumno in materias_reprobadas:
            for materia in alumno.materias:
                if materia.anio == año and materia.nota < aprueba_con:
                    alumnos_reprobados.append(alumno.nombre)
        return alumnos_reprobados
                


    def alumnos_egresados(self, aprueba_con):
        egresados = list()
        for alumno in self.alumnos:
            if not alumno.materias_desaprobadas(aprueba_con):
                egresados.append(alumno.nombre)
        return egresados

alumno1 = Alumno("Facundo", "Duran", 24, 1, lista_materias_1)
alumno2 = Alumno("Camila","Perez", 26, 2, lista_materias_2)
academia1 = Academia("Da Vinci", [alumno1, alumno2])
print(academia1.alumnos_reprobados(2021, 4))