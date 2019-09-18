from peewee import *
from datetime import * #importo libreria de fechas

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

def create_family_member():

    #FORMA 1 DE INSERTAR
    tio_tommy = Person(name = "Tommy", birthday = date(2000,11,10),is_relative = True)
    tio_tommy.save()

    #FORMA 2 DE INSERTAR(MÁS SENCILLA)
    abuela_nona = Person.create(name = "Nona", birthday = date(1956,11,10),is_relative = False)


    #crearé algunas mascotas y las asocio mediante la ForeignKeyField
    tommys_dino = Pet.create(owner = tio_tommy, name = "Reptar", animal_type = "Dinosaurio")
    tommys_snake = Pet.create(owner = abuela_nona, name = "Viborita", animal_type = "Boa Constrictor")






#Llamo a la función de conexión
create_and_connect()

#Llamo a la función que inserta en la # DEBUG:
create_family_member()
print()
input("Felicidades, registros insertados correctamente, presione ENTER para salir...")
