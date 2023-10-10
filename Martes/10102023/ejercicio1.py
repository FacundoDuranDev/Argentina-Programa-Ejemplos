# Desarrolle un módulo/archivo para las clases Materia
# y Alumno desarrolladas en el punto II (uno para cada una)
# y luego desarrolle la clase Academia que importe ambas clases.
# La clase academia debe contar con las siguientes funciones:
# Cantidad de alumnos aprobados por año:
#  retorna la cantidad de alumnos con todas las materias aprobadas de un año pasado por parámetro.
# Alumnos egresados: 
# retorna una lista de los alumnos que tienen todas las materias aprobadas.
from classes.Academia.Materia import Materia
from classes.Academia.Alumno import Alumno

class Academia:
    def __init__(self, nombre_academia, alumnos):
        self.nombre = nombre_academia
        self.alumnos = alumnos

    def alumnos_reprobados(self, aprueba_con):
        reprobados = list()
        for alumno in self.alumnos:
            if alumno.materias_desaprobadas(aprueba_con):
                reprobados.append(alumno.nombre)
        return reprobados
 
    def alumnos_egresados(self, año, aprueba_con):
        egresados = list()
        materias_anuales = list()
        lista_desaprobado = list()
        for alumno in self.alumnos:
            for materia in alumno.materias:
                if materia.anio == año:
                    materias_anuales.append({"alumno": alumno.nombre, "materia": materia})
        for diccionario in materias_anuales:
            if diccionario["materia"].nota >= aprueba_con:
                print(diccionario)
            else:
                lista_desaprobado.append(diccionario["alumno"])
        for alumno in self.alumnos:
            if not alumno.nombre in lista_desaprobado:
                egresados.append(alumno)
        return egresados
        
            

lista_materias_1 = [
    Materia("Historia",2021, 7),
    Materia("Matemáticas", 2021, 5),
    Materia("Historia",2022, 7),
    Materia("Matemáticas", 2022, 7),
    Materia("Historia",2023, 7),
    Materia("Matemáticas", 2023, 4),
    Materia("Geografía",2021, 2),
    Materia("Conocimiento del Medio", 2023, 5),
]
lista_materias_2 = [
    Materia("Historia",2021, 4),
    Materia("Matemáticas", 2021, 6),
    Materia("Historia",2022, 9),
    Materia("Matemáticas", 2022, 6),
    Materia("Historia",2023, 8),
    Materia("Matemáticas", 2023, 5),
    Materia("Geografía",2021, 5),
    Materia("Conocimiento del Medio", 2023, 10),
]                      
alumno1 = Alumno("Facundo", "Duran", 24, 1, lista_materias_1)
alumno2 = Alumno("Camila","Perez", 26, 2, lista_materias_2)
print(alumno2.mejor_materia())
academia1 = Academia("UBA", [alumno1, alumno2])
academia1.alumnos_egresados(2021, 4)