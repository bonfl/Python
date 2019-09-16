def clear_screen():
    import os
    os.system ("clear")
clear_screen()







def agregar_articulo(articulo):
    archivo_lista = open("archivo.txt","a")
    archivo_lista.write ("{} \n".format(articulo))
    archivo_lista.close()
 
agregar_articulo(input("Articulo que deseas agregar: "))
