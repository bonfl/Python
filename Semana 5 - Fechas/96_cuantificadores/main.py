def clear_screen():
    import os
    os.system ("clear")
clear_screen()


#Importar libreria de archivos
import re

#Abro el archivo
archivo = open("sample.txt",encoding="utf-8")

#leo el archivo
informacion = archivo.read()

#Lo cierro para liberar memoria
archivo.close()


print()
print()
#voy a buscar por formato de numero telefonico
#me ayudo en regexr.com para armar el formato
#segun regexr.com, para el numero +9-555-(237)-2468
#el formato seria \+\d-\d\d\d-\(\d\d\d\)-\d\d\d\d
#pruebo impresion en pantalla
#Comparar con ejercicio 95 para ver las expresiones regulares cuantificadsa
#el signo de interrogacion dice que el + es opcional...
print(re.search(r"\+?\d-\d{3}-\(\d{3}\)-\d{4}",informacion))
print()




input("Presione ENTER para salir...")
