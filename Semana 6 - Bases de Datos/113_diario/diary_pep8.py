# Importo librería de peewee
from peewee import *

# traigo libreria de fechas
import datetime

# Libreria de diccionarios ordenados
from collections import OrderedDict

# utilidad
import sys


# Clase desde la 113 hasta la 122
def clear_screen():
    import os
    os.system("clear")

clear_screen()


# Llamo a mi DB, si no existe, la crea
db = SqliteDatabase("diary.db")


# mi tabla...
class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def menu_loop():
    """Show menu"""
    clear_screen()
    choice = None
    while choice != "q":
        print("Press q to quit")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice = input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()


def add_entry():
    """Add Entry"""
    print("Enter your thoughts. Press Ctrl + D to finish")
    data = sys.stdin.read().strip()

    if data:
        if input("Do u want to save your entry? [Y/n]").lower().strip() != "n":
            Entry.create(content=data)
            print("Your Entry was saved successfully")


def view_entries(search_query=None):
    """View All Entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())

    # para ver si utilizará la búsqueda del search 1 entry
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime("%A %B %d, %Y %I %M%p")
        print(timestamp)
        print("+" * len(timestamp))
        print()
        print(entry.content)
        print()
        print("+" * len(timestamp))
        print("n) next entry")
        print("e) edit entry")
        print("d) delete entry")
        print("q) Return to menu")

        next_action = input("Action: ").lower().strip()
        if next_action == "q":
            break
        elif next_action == "d":
            delete_entry(entry)
        elif next_action == "e":
            edit_entry(entry)


def delete_entry(entry):
    """Delete an Entry"""
    action = input("Are you sure? y/n").lower().strip()

    if action == "y":
        entry.delete_instance()


def edit_entry(entry):
    """Edit an Entry"""

    print("Edit your thoughts. Press Ctrl + D to finish")
    entry_edited = sys.stdin.read().strip()
    action = input("Are you sure? y/n").lower().strip()

    if action == "y":
        entry.content = entry_edited
        entry.save()


# guardo texto a buscar
def search_entries():
    """Search entries"""
    search_query = input("Search query: ").strip()
    view_entries(search_query)


# mi lista ordenada
menu = OrderedDict([
    ("a", add_entry),
    ("v", view_entries),
    ("s", search_entries),
    ("d", delete_entry)
])


# Defino función que crea y conect a la DB
def create_and_connect():
    """Connects to the DB and create the tables"""
    db.connect()
    db.create_tables([Entry], safe=True)


# Este if hace que se ejecute desde python3.7 y no desde otros lados.
if __name__ == '__main__':
    create_and_connect()
    menu_loop()

print()
input("ENTER to exit...")
clear_screen()
