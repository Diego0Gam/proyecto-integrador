from peewee import Model, AutoField, CharField, DateField
from basedatos.db import db

class Curso(Model):
    curso_id = AutoField()
    nombre = CharField(unique=True)
    descripcion = CharField()
    fecha_inicio = DateField()
    fecha_fin = DateField()
    horas = CharField()

    class Meta:
        database = db
        table_name = 'cursos'