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

#Imprimo en pantalla la informacion del archivo
print("---------- ACA COMIENZA EL ARCHIVO -------------")
print()
print(informacion)
print()
print("---------- ACA FINALIZA EL ARCHIVO -------------")
print()


#Ahora realizare un match contra alguna cadena de texto que este en sample.txt
#llamo a la lib RE, uso match, con R busco, busca todo en la variable informacion
print(re.match(r"abcdefghijklmnñopqrstuvwxyz",informacion))

#El match sirve solo para la 1er fila, si quiero encontrar en todo el archivo
print()
print()
print(re.search(r"0123456789",informacion))

input("Presione ENTER para salir...")
