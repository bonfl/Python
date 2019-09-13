
from player import Player




#Creo una instancia de la clase player
#Estoy creando un objeto, usando la clase player
#Imprimo la clase con los valores x defecto
sorcerer = Player()

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
knight = Player(1000,4000,"Caballero","Rayo Cosmico")



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
#creo otra variable llamando a la clase player
paladin = Player(2310,2,"Paladin","Puffi Puffi iaiaia")
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
#creo otra variable llamando a la clase player
druid = Player(60000000,20,"Druid","Chancletazos")
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
