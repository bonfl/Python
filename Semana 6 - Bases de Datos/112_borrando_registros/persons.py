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
    abuela_rosa = Person.create(name = "Rosa", birthday = date(1956,11,10),is_relative = False)

    #crearé algunas mascotas y las asocio mediante la ForeignKeyField
    tommys_dino = Pet.create(owner = tio_tommy, name = "Reptar", animal_type = "Dinosaurio")
    tommys_snake = Pet.create(owner = abuela_nona, name = "Viborita", animal_type = "Boa Constrictor")

    #Modifico el nombre y guardo
    tommys_dino.name = "Rex"
    tommys_dino.save()

#Obtener datos de la tabla entera
def get_family_members():
    for person in Person.select():
        print("Nombre: {} con fecha de nacimiento: {}".format(person.name,person.birthday))

#Obtener datos de 1 persona en base a lo ingresado cuando llamo a la funcion
def get_family_member(name):
    family_member = Person.select().where(Person.name == name).get()#con el get le digo que solo es 1 registro
    print("{} cumple el: {}".format(name, family_member.birthday))
    print()

#Otra forma de obtener los registros de 1 persona.
def get_family_member2(name):
    family_member = Person.get(Person.name == name)
    print("{} cumple el: {}".format(name, family_member.birthday))


def delete_pet(name):
    query = Pet.delete().where(Pet.name == name)
    deleted_entries = query.execute()
    print("registros borrados: {}".format(deleted_entries))


#esta forma borra solo de a 1 registro
def delete_pet2(name):
        query = Pet.get(Pet.name == name)
        deleted_entry = query.delete_instance()
            print("registros borrados: {}".format(deleted_entry))




#Llamo a la función de conexión
create_and_connect()
#Llamo a la función que inserta en la # DEBUG:
#create_family_member()
#Llamo a la funcion que llama a la tabla Person
#get_family_members()
print()
#llamo a la funcion con valor de entrada ROSA
#get_family_member("Rosa")

#llamo a mi funcion mejorada
#get_family_member2(input("Ingrese Nombre a buscar en la tabla: "))
print()

#llamo a la funcion que borra registros
delete_pet("Viborita")

#llamo a la 2da forma definida para borrar registros
delete_pet2("Rex")

input("FIN, presione ENTER para salir...")
