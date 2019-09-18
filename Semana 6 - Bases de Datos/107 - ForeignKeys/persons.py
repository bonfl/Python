from peewee import *

#Me conecto a la base de datos persona.db, si no existe, la crea
db = SqliteDatabase('persona.db')

#Esta clase armará la tabla Person
class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()
    class Meta:
        database = db

#Esta clase armará la tabla Pet
class Pet(Model):
    owner = ForeignKeyField(Person, related_name= 'pets')
    name = CharField()
    animal_type = CharField()
    #por que tengo que poner el class meta 2 vecesss???
    class Meta:
        database = db

#defino función de conex
def create_and_connect():
    db.connect()
    #Acá crearé las tablas, el safe true indica que pasará x arriba la .db existente
    db.create_tables([Person,Pet], safe = True)

#Llamo a la función
create_and_connect()
