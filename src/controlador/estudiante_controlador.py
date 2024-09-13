from servicio.estudiante_servicio import EstudianteServicio

class EstudianteControlador():
    
    def crear(nombre, dni, email, telefono, fecha_nacimiento, curso_id):
        return EstudianteServicio.crear_estudiante(nombre, dni, email, telefono, fecha_nacimiento, curso_id)
    
    def mostrar():
        return EstudianteServicio.mostrar_estudiantes()
    
    def eliminar(estudiante_id):
        return EstudianteServicio.eliminar_estudiante(estudiante_id)