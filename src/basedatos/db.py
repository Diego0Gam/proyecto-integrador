from peewee import MySQLDatabase

# Local
db = MySQLDatabase(
    'db_crud',
    user='root',
    password='',
    host='localhost',
    port=3306
)