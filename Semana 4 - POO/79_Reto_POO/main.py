#video 72
def clear_screen():
    import os
    os.system ("clear")
clear_screen()


#probando commit
#Importa toda la libreria player.py
import player


sorcerer = player.Sorcerer(hit_points = 40, mana = 80)
knight = player.Knight(hit_points = 433, mana = 8080)
paladin = player.Paladin()
enano = player.Enano()
druid = player.Druid(hit_points = 433, mana = 8080)
troll = player.Troll()
island_troll = player.Island_Troll()



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
print()
print(troll)
print()
print(island_troll)
input()
print()
print("Fin del programa!!!!")
input()
