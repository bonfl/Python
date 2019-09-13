#video 72
#Esto es mi clase
# Visualizo 3 formas distintas de agregarle valores a mi clase
class Player:
# FORMA 1
    vocation = "No Vocationn"
    hechizo = "Puff"
    movement_speed = 50

# FORMA 2
    #Defino el método INIT, creando valores por defecto para los atributos
    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",500)
        self.mana = kwargs.get("mana",70)

    def __str__(self):
        #Devuelvo una cadena
        return "El {} tiene: {} de Hit Points y {} de Mana y puede lanzar {} y tiene {} de Velocidad".format(self.vocation,
                                                                                                             self.hit_points,
                                                                                                             self.mana,
                                                                                                             self.hechizo,
                                                                                                             self.movement_speed)


#FORMA 3
    #Defino un método
    def lanzar_hechizo(self):
      return self.hechizo
#--------------------------------------------------------------------------
# Le estoy diciendo que cree la clase Sorcerer heredando valores de la clase Player
class Sorcerer(Player):
    vocation = "Sorcererrrus"
    hechizo = "Utevo Luxim"
    movement_speed = 20

# Le estoy diciendo que cree la clase Knight heredando valores de la clase Player
class Knight(Player):
    vocation = "Knighttttt"
    hechizo = "Pufac"

# Le estoy diciendo que cree la clase Paladin heredando valores de la clase Player
class Paladin(Player):
    vocation = "Paladin"
    hechizo = "Paladin iaiaia"
    movement_speed = 50000

# Le estoy diciendo que cree la clase Enano heredando valores de la clase Player
class Enano(Player):
    vocation = "Enano"
    hechizo = "patada corta"
    movement_speed = 2

# Le estoy diciendo que cree la clase Druid heredando valores de la clase Player
class Druid(Player):
    vocation = "Druid"
    hechizo = "Druid attackkkkk"
    movement_speed = 1
