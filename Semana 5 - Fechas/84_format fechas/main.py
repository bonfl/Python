#Video 84 -- formateando fechas
def clear_screen():
    import os
    os.system ("clear")
clear_screen()

#Importo libreria de fechas y hs
import datetime

now = datetime.datetime.now()
print(now)
print()
now = now.strftime("%B %d, %Y")
print("La fecha en el nuevo formato es: {}".format(now))
# linea 14 es igualue hacer un print("la fecha es..",now)
print()

#si tengo una variable con una fecha en formato cadena, ejemplo:
fecha_cadena = input("Ingrese fecha: ")
print ("La fecha en formato cadena es {}".format(fecha_cadena)) #esta fecha en formato cadena no sirve para mucho...
print()
#convierto mi string a fecha.

fecha_formateada = datetime.datetime.strptime(fecha_cadena,"%d/%m/%Y")
print()
print ("La fecha en formato fecha(convertida del string anterior) es {}".format(fecha_formateada))
print()
input("Gracias, presione ENTER para salir...")
