from classes.Academia.Academico import Academico
from classes.Academia.Materia import Materia
from classes.Academia.Alumno import Alumno

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
academia1 = Academico("UBA", [alumno1, alumno2])
print(academia1.alumnos_graduados(4))
