#Video 82 --
def clear_screen():
    import os
    os.system ("clear")
clear_screen()

#Importo libreria de fechas y hs
import datetime


now = datetime.datetime.now()
print(now)
print()
#si quiero adelantar 5 dias a futuro

now = now + datetime.timedelta(days = 5)
print(now)

print()
#si quiero adelantar 5 dias a futuro pero tambien minutos y segundos..
now = now + datetime.timedelta(days = 5, hours = 12, seconds = 8)
print(now)
print()

print()
#si quiero retroceder 5 dias ..
now = now + datetime.timedelta(days = -5) # o sino now - datetime.timedelta
print(now)
print()

#si quiero ver solo la fecha pero no la hora
now2 = now.date()
print(now)
print()
print()

#si quiero ver solo la hora pero no la fecha
now = now.time()
print(now)
print()
input()
