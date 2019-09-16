def clear_screen():
    import os
    os.system ("clear")
clear_screen()


# Es muy similar a los ejercicios anteriores, pero utilizo la bandera w.
archivo_lista = open("archivo.txt","w")
archivo_lista.write ("Titulo: Creando mi primer archivo en Python\n")
archivo_lista.write ("\n")
archivo_lista.write ("Cuerpo del archivo")
archivo_lista.close()




input("Archivo creado exitosamente. Presione ENTER para salir...")

#Este codigo sobreescribe al archivo N veces
