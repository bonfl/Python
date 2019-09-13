from player import Player

print()


#Creo una instancia de la clase player
#Estoy creando un objeto, usando la clase player
sorcerer = Player() #Imprimo la clase con los valores x defecto
#sorcerer.hit_points = 50
#sorcerer.mana = 4
#sorcerer.vocation = "Mago"

#Imprimo el resultado en pantalla
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
