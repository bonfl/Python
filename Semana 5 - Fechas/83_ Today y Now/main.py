#Video 83 --
def clear_screen():
    import os
    os.system ("clear")
clear_screen()

#Importo libreria de fechas y hs
import datetime


now = datetime.datetime.now()
print(now)
print()

#el today es parecido al now, pero al now se le puede pasar zona horaria
today = datetime.datetime.today()
print(today)

#Esto me mostrara las horas en cero
variable2 = datetime.time()
print(variable2)
print()

#si quiero traer el dia de hoy pero la hora en cero, tengo que combinar

variable3 = datetime.datetime.combine(datetime.datetime.today(),datetime.time())
print (variable3)
