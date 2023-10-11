
class Alumno:
  def __init__(self, nombre, apellido, edad, dni, materias):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.dni = dni
    self.materias = materias

  def obtener_promedio_anual(self, anio):
    materias_anuales = list()
    for materia in self.materias:
      if materia.anio == anio:
        materias_anuales.append(materia.nota)
    return sum(materias_anuales) // len(materias_anuales)

  def obtener_promedio_general(self):
    promedio_general = list()
    for materia in self.materias:
      promedio_general.append(materia.nota)
    return sum(promedio_general) // len(promedio_general)

  def mejor_materia(self):
    notas = [
        materia.nota for materia in self.materias
        # for materia in self.materias:
        #     materia.nota 
    ]
    lista_retorno = list()
    nota_maxima = max(notas)
    for materia in self.materias:
      if materia.nota == nota_maxima:
        lista_retorno.append((materia.nombre, materia.nota, materia.anio))
    return lista_retorno
  def materias_desaprobadas(self, aprueba_con):
    desaprobadas = list()
    for materia in self.materias:
      if materia.nota < aprueba_con:
        desaprobadas.append(
            {
                "nombre": materia.nombre,
                "nota":materia.nota,
                "año":materia.anio,
            }
        )
    return desaprobadas