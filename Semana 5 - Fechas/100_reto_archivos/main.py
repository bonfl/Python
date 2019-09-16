def clear_screen():
    import os
    os.system ("clear")
clear_screen()

import re

def banner():
    print("-----------------------------------|")
    print("-         PENDIENTES  1.0          |")
    print("-----------------------------------|")



#Defino funcion para agregar datos al archivo
def agregapendiente(pendiente):
    clear_screen()
    banner()
    archivo_lista = open("archivodependientes.txt","a")
    archivo_lista.write ("{} \n".format(pendiente))
    archivo_lista.close()
    print()
    input("Pendiente cargado. Presione ENTER para volver al menú principal...")
    clear_screen()

#Defino funcion para ver el archivo completo
def verpendiente():
    clear_screen()
    banner()
    archivo = open("archivodependientes.txt",encoding="utf-8")
    #leo el archivo
    informacion = archivo.read()
    #Lo cierro para liberar memoria
    archivo.close()
    #Imprimo en pantalla la informacion del archivo
    print()
    print("Los pendientes en este momento son: \n\n{}".format(informacion))
    print()
    input("Presione ENTER para volver al menú principal...")
    clear_screen()



def iniciar_pendientes():

    while True:
        banner()
        print("                                   |")
        print("1 - Agregar pendientes             |")
        print("2 - Ver pendientes                 |")
        print("0 - Salir del programa             |")
        print()
        #Controlo caracteres invalidos
        try:
            opcion = int(input(" Ingrese opcion: "))
        #Capturo el error
        except ValueError:
            input("Debes seleccionar un numero, presione ENTER para reintentar...")
            clear_screen()
        else:
            if opcion == 1:
                #acá llamo a la funcion
                agregapendiente(input("Ingrese un nuevo pendiente: "))
            elif opcion == 2:
                #llamo a la funcion
                verpendiente()
            elif opcion == 0:
                clear_screen()
                break


iniciar_pendientes()
