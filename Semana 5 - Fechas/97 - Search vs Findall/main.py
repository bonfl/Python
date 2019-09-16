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
#el search solo busca 1 match, el findall encuentra todos...
print(re.findall(r"\+?\d-\d{3}-\(\d{3}\)-\d{4}",informacion))
print()

# si quiero mostrarlo un poco mas prolijo
agrupacion = re.findall(r"\+?\d-\d{3}-\(\d{3}\)-\d{4}",informacion)
print("El resultado de la busqueda es: {}".format(agrupacion))



input("Presione ENTER para salir...")
