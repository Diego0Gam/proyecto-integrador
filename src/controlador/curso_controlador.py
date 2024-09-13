from servicio.curso_servicio import CursoServicio

class CursoControlador():
    
    def crear(nombre, descripcion, fecha_inicio, fecha_fin, horas):
        return CursoServicio.crear_curso(nombre, descripcion, fecha_inicio, fecha_fin, horas)
    
    def mostrar():
        return CursoServicio.mostrar_cursos()