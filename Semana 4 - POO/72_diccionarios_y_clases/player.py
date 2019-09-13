#video 72
#Esto es mi clase
class Player:

    #Defino el método INIT, creando valores por defecto para los atributos
    def __init__(self,**kwargs):
        self.hit_points = kwargs.get("hit_points",500)
        self.mana = kwargs.get("mana",70)
        self.vocation = kwargs.get("vocation","No vocation")
        self.rayox = kwargs.get("rayox","Pufffffiiiaa")

    #Defino un método
    def lanzar_rayox(self):
      return self.rayox
