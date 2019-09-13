#video 72
#Esto es mi clase
# Visualizo 3 formas distintas de agregarle valores a mi clase
class Player:
# FORMA 1
    vocation = "No Vocationn"
    hechizo = "Puff"
    movement_speed = 50
    hit_points = 700
    mana = 1079

# FORMA 2 --
    #Defino el método INIT, creando valores por defecto para los atributos
    def __init__(self,**kwargs):
        self.nombre = input("Elige un nombre para tu jugador: ")


    def __str__(self):
        #Devuelvo una cadena
        return "{} es un {} y tiene: {} de Hit Points, {} de Mana y puede lanzar {} Tiene {} de Velocidad".format(self.nombre,
                                                                                                                  self.vocation,
                                                                                                                  self.hit_points,
                                                                                                                  self.mana,
                                                                                                                  self.hechizo,
                                                                                                                  self.movement_speed)


#FORMA 3
    #Defino un método
    def lanzar_hechizo(self):
        self.hechizo
#--------------------------------------------------------------------------
# Le estoy diciendo que cree la clase Sorcerer heredando valores de la clase Player
class Sorcerer(Player):
    vocation = "Sorcererrrus"
    hechizo = "Utevo Luxim"
    movement_speed = 20


# Le estoy diciendo que cree la clase Knight heredando valores de la clase Player
class Knight(Player):
    vocation = "Knighttttt"
    hechizo = "hadouken"
    #Estoy diciendole que sobreescriba el metodo definido en la linea 29 y  30.
    def lanzar_hechizo(self):
      return "{} y Exura".format(self.hechizo)

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
    def lanzar_hechizo(self):
        return "{} y Exura".format(self.hechizo)

class Troll(Player):
    vocation = "Troll"
    hechizo = "hechizo que tiran los trolls"
    hit_points = 20000
    mana = 10
    #movement_speed = 10000


class Island_Troll(Troll):
    vocation = "Island Troll"
    hit_points = 15000
