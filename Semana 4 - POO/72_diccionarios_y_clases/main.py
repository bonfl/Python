#video 72
def clear_screen():
    import os
    os.system ("clear")
clear_screen()

#Llamo a la clase player.py
from player import Player




#Creo una instancia de la clase player
#Estoy creando un objeto, usando la clase player
sorcerer = Player(hit_points = 40, mana = 80, vocation = "sorcerrerrr", rayox = "utevolux")

print()
print("Ahora creo un objeto, utilizando la clase Player, El sorcerer tiene: ")
print()
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)

#Acá llamo a mi método, creado en la clase. Los métodos SOLO pueden estar adentro de los objetos, pero no sueltos.
print(sorcerer.lanzar_rayox())


print()
print()


#---------------------------------


#Creo una instancia de la clase player
#Estoy creando un objeto, usando la clase player
#Le cambio los valores by default de la clase.
knight = Player(hit_points = 433, mana = 8080, vocation = "caballero", rayox = "cabaiaaaa")

#Imprimo el resultado en pantalla
print("Ahora creo otro objeto, utilizando la clase Player, el Caballero tiene: ")
print()
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
#Acá llamo a mi método, creado en la clase. Los métodos SOLO pueden estar adentro de los objetos, pero no sueltos.
print(knight.rayox)
print()
print()

#---------------------------------
#creo otra instancia llamando a la clase player
paladin = Player(hit_points = 1, mana = 2, vocation = "paladin", rayox = "no tiene")
#Imprimo el resultado en pantalla
print("Ahora creo otro objeto, utilizando la clase Player, el Paladin tiene: ")
print()
print(paladin.hit_points)
print(paladin.mana)
print(paladin.vocation)
#Acá llamo a mi método, creado en la clase. Los métodos SOLO pueden estar adentro de los objetos, pero no sueltos.
print(paladin.rayox)
print()
print()

#---------------------------------
#creo otra instancia llamando a la clase player
druid = Player(hit_points = 900, mana = 98, vocation = "druid", rayox = "chancletazos")
#Imprimo el resultado en pantalla
print("Ahora creo otro objeto, utilizando la clase Player, el Druid tiene: ")
print()
print(druid.hit_points)
print(druid.mana)
print(druid.vocation)
#Acá llamo a mi método, creado en la clase. Los métodos SOLO pueden estar adentro de los objetos, pero no sueltos.
print(druid.rayox)
print()
print()
input()

#---------------------------------
#creo otra instancia llamando a la clase player
enano = Player()
#Imprimo el resultado en pantalla
print("Ahora creo otro objeto, utilizando la clase Player, el enano tiene: ")
print()
print(enano.hit_points)
print(enano.mana)
print(enano.vocation)
#Acá llamo a mi método, creado en la clase. Los métodos SOLO pueden estar adentro de los objetos, pero no sueltos.
print(enano.rayox)
print()
print()
input()
