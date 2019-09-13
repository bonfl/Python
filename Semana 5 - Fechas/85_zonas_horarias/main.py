#Video 84 -- formateando fechas
def clear_screen():
    import os
    os.system ("clear")
clear_screen()

#Importo libreria de fechas y hs
import datetime

central_time = datetime.timezone(datetime.timedelta(hours = -6))
print()


pacific_time = datetime.timezone(datetime.timedelta(hours = -8))

print()
eastern_time = datetime.timezone(datetime.timedelta(hours = -5))

print()
print(datetime.datetime.now(pacific_time))
input()
