#video 72
def clear_screen():
    import os
    os.system ("clear")
clear_screen()



#Importa toda la libreria player.py
import player


sorcerer = player.Sorcerer(hit_points = 40, mana = 80)
knight = player.Knight(hit_points = 433, mana = 8080 ,hechizo = "cabaiaaaa")
paladin = player.Paladin()
enano = player.Enano()
druid = player.Druid(hit_points = 433, mana = 8080 ,hechizo = "cabaiaaaa")



print()
print()
print(sorcerer)
print()
print(knight)
print()
print(paladin)
print()
print(enano)
print()
print(druid)
input()
print("Fin del programa!!!!")
input()
