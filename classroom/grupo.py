from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def _init_(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        if estudiantes==None:
            estudiantes=[]
        if asignaturas==None:
            asignaturas=[]
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista==None:
            lista=[]
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def _str_(self):
        return("Grupo de estudiantes: "+self._grupo)

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre