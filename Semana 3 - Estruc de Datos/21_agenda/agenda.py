def clear_screen():
    import os
    os.system ("clear")
clear_screen()


# PARA REPL.IT COPIAR DESDE ESTA LINEA
def iniciar_agenda():

    print("-----------------------------------|")
    print("-           AGENDA 1.0             |")
    print("-----------------------------------|")


    def imprimir_mensaje(mensaje):
        print()
        print("-------------------------")
        print(mensaje)
        print("-------------------------")
        print()


    def agregarcontac():
        nombre = input("Ingrese nombre del contacto: ")
        numero = input("Ingrese numero del contacto: ")
        agenda_telefonica[nombre] = numero
        imprimir_mensaje("Contacto agregado exitosamente")


    def ver1contac():
        nombre = input("Ingrese nombre del contacto: ")
        try:
            print(nombre + " -> " + agenda_telefonica[nombre])
        except KeyError:
            print("Ese contacto no existe")
        else:
            print()

    def verallcontac():
        if len(agenda_telefonica) == 0:
            print("No existen contactos todavia")
        else:
            for contacto in agenda_telefonica:
                print(contacto + " -> " + agenda_telefonica[contacto])


    def borrarcontac():
        try:
            nombre = input("Ingrese nombre del contacto a borrar: ")
            del agenda_telefonica[nombre]
            imprimir_mensaje("Contacto borrado exitosamente")
        except KeyError:
            print ("Contacto inexistente")
        else:
            print()


    def updatecontac():
        nombre = input("Ingrese nombre del contacto: ")
        numero = input("Ingrese numero del contacto: ")
        agenda_telefonica[nombre] = numero
        imprimir_mensaje("Contacto modificado exitosamente")


    agenda_telefonica = dict()

    while True:
        print("                                   |")
        print("1 - Agregar Contacto               |")
        print("2 - Borrar Contacto                |")
        print("3 - Actualizar Contacto            |")
        print("4 - Visualizar 1 contacto          |")
        print("5 - Visualizar todos los contactos |")
        print("0 - Salir del programa             |")
        print
        #Controlo caracteres invalidos
        try:
            opcion = int(input(" Ingrese opcion: "))
        #Capturo el error
        except ValueError:
            print("Debes seleccionar un numero")
        else:
            if opcion == 1:
                agregarcontac()
            elif opcion == 2:
                borrarcontac()
            elif opcion == 3:
                updatecontac()
            elif opcion == 4:
                ver1contac()
            elif opcion == 5:
                verallcontac()
            elif opcion == 0:
                break
iniciar_agenda()
