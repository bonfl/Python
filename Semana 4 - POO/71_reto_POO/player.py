
#Esto es mi clase
class Player:

    #Defino el método INIT, creando valores por defecto para los atributos
    def __init__(self,hit_points = 10,mana = 10,vocation= "No Vocation",rayox = "Puff"):
        self.hit_points = hit_points
        self.mana = mana
        self.vocation = vocation
        self.rayox = rayox

    #Defino un método
    def lanzar_rayox(self):
      return self.rayox
