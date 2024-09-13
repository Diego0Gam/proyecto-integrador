from basedatos.db import db
from modelo.cursos import Curso
from modelo.estudiantes import Estudiante
from controlador.curso_controlador import CursoControlador
from controlador.estudiante_controlador import EstudianteControlador

def main():
    db.connect()
    db.create_tables([Curso, Estudiante])

    #CursoControlador.crear("Programacion II", "Curso introductorio a la programacion", "2024-01-01", "2024-06-30", "15:00-17:00")
    cursos = CursoControlador.mostrar()
     
    for curso in cursos:
        print(f"{curso.curso_id} {curso.nombre}")

    #EstudianteControlador.crear("Juan", 52025252, "alexispuca@gmail.com", 3245342, "2007-02-07", 2)
    EstudianteControlador.eliminar(3)
    
if __name__ == '__main__':
    main()