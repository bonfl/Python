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
print("El {} tiene: {} de Hit Points y {} de Mana y puede lanzar: {}".format(sorcerer.vocation,
                                                                             sorcerer.hit_points,
                                                                             sorcerer.mana,
                                                                             sorcerer.hechizo))

print("El {} tiene: {} de Hit Points y {} de Mana y puede lanzar: {}".format(knight.vocation,
                                                                             knight.hit_points,
                                                                             knight.mana,
                                                                             knight.hechizo))

print("El {} tiene: {} de Hit Points y {} de Mana y puede lanzar: {}".format(paladin.vocation,
                                                                             paladin.hit_points,
                                                                             paladin.mana,
                                                                             paladin.hechizo))

print("El {} tiene: {} de Hit Points y {} de Mana y puede lanzar: {}".format(enano.vocation,
                                                                             enano.hit_points,
                                                                             enano.mana,
                                                                             enano.hechizo))

print("El {} tiene: {} de Hit Points y {} de Mana y puede lanzar: {}".format(druid.vocation,
                                                                             druid.hit_points,
                                                                             druid.mana,
                                                                             druid.hechizo))
input()
print("Fin del programa!!!!")
input()
