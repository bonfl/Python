from player import Player

print()


print("Primero imprimo la clase vacía")
print()
print(Player.hit_points)
print(Player.mana)
print(Player.vocation)
print()
print()



#Creo una instancia de la clase player
#Estoy creando un objeto, usando la clase player
sorcerer = Player()
sorcerer.hit_points = 50
sorcerer.mana = 4
sorcerer.vocation = "Mago"

#Imprimo el resultado en pantalla
print("Ahora creo un objeto, utilizando la clase Player")
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
knight = Player()
knight.hit_points = 100
knight.mana = 4000
knight.vocation = "Caballero"
knight.rayox = "iaaaaiaiaiaiaiaaaaa"
#Imprimo el resultado en pantalla
print("Ahora creo otro objeto, utilizando la clase Player")
print()
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
#Acá llamo a mi método, creado en la clase. Los métodos SOLO pueden estar adentro de los objetos, pero no sueltos.
print(knight.rayox)
print()
print()
input()
