
#Importar libreria de archivos
import re

#Abro el archivo
archivo = open("sample.txt",encoding="utf-8")

#leo el archivo
informacion = archivo.read()

#Lo cierro para liberar memoria
archivo.close()

#Imprimo en pantalla la informacion del archivo
print(informacion)
