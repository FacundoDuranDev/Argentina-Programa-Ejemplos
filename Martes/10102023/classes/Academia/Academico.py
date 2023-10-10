class Academico:
  def __init__(self, nombre_institucion, alumnos):
    self.nombre = nombre_institucion
    self.alumnos = alumnos

  def promedio_general(self):
    promedio_general = list()
    for alumno in self.alumnos:
      promedio_general.append(
        alumno.obtener_promedio_general()
      )
    return sum(promedio_general) // len(promedio_general)

  def alumnos_graduados(self, aprueba_con):
    graduados = list()
    for alumno in self.alumnos:
      if not alumno.materias_desaprobadas(aprueba_con):
        # => con el not, anulabamos la condición invirtiendo el comportamiento
        # => si esto da falso, va a ejecutar este codigo
        # dentro de un condicional una lista vacía cuenta como "False"
        graduados.append(alumno.nombre)
    return graduados