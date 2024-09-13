from modelo.estudiantes import Estudiante
from modelo.cursos import Curso

class EstudianteServicio:

    @staticmethod
    def crear_estudiante(nombre, dni, email, telefono, fecha_nacimiento, curso_id):
        curso = Curso.get(Curso.curso_id==curso_id)
        estudiante = Estudiante.create(nombre=nombre, dni=dni, email=email, telefono=telefono, fecha_nacimiento=fecha_nacimiento, curso_id=curso_id)
        return estudiante

    @staticmethod
    def mostrar_estudiantes():
        return list(Estudiante.select())
    
    @staticmethod
    def eliminar_estudiante(estudiante_id):
        estudiante = Estudiante.get(Estudiante.estudiante_id == estudiante_id)
        estudiante.delete_instance()
        return estudiante