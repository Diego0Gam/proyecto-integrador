from peewee import Model, AutoField, CharField, DateField, IntegerField, ForeignKeyField
from basedatos.db import db
from modelo.cursos import Curso

class Estudiante(Model):
    estudiante_id = AutoField()
    nombre = CharField()
    dni = IntegerField(unique=True)
    email = CharField()
    telefono = IntegerField()
    fecha_nacimiento = DateField()
    curso_id = ForeignKeyField(Curso)

    class Meta:
        database = db
        table_name = 'estudiantes'