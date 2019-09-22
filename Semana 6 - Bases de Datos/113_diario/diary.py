#Clase desde la 113 hasta la 122
#Importo librería de peewee
from peewee import *

#traigo libreria de fechas
import datetime

#Libreria de diccionarios ordenados
from collections import OrderedDict

#utilidad
import sys

# Llamo a mi DB, si no existe, la crea
db = SqliteDatabase("diary.db")





#mi tabla...
class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def menu_loop():
    """Show menu"""
    choice = None
    while choice != "q":
        print("Press q to quit")
        for key,value in menu.items():
            print ("{}) {}".format(key,value.__doc__))
        choice = input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()

def add_entry():
    """Add Entry"""
    print("Enter your thoughts. Press Ctrl + D to finish")
    data = sys.stdin.read().strip()

    if data:
        if input ("Do you want to save your entry? [Y/n]").lower().strip() != "n":
            Entry.create(content = data)
            print("Your Entry was saved successfully")


def view_entries():
    """View All Entries"""

def delete_entry():
        """Delete an Entry"""


#mi lista ordenada

menu = OrderedDict([
        ("a",add_entry),
        ("v",view_entries),
        ("d",delete_entry)
    ])

#Defino función que crea y conect a la DB
def create_and_connect():
    """Connects to the DB and create the tables"""
    db.connect()
    db.create_tables([Entry],safe = True)

#Este if hace que se ejecute el llamado solo desde python3.7 y no desde otros lados.
if __name__ == '__main__':
    create_and_connect()
    menu_loop()
