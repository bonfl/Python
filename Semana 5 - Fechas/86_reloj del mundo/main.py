def clear_screen():
    import os
    os.system ("clear")
clear_screen()

#Importo libreria de fechas y hs
import datetime


# PARA REPL.IT COPIAR DESDE ESTA LINEA
def iniciar_reloj():



    def imprimir_mensaje(mensaje):
        print()
        print("-----------------------------------|")
        print(mensaje)
        print("-----------------------------------|")
        print("                                   |")


                    #La funcion horageneral aceptara un parametro zona_horaria
    def horageneral(zona_horaria):
        formato = "%H:%M:%S"
        print()
        
        #Para que en el print muestre la ciudad
        if zona_horaria == -3:
            zona = "Uruguay"
        elif zona_horaria == -5:
            zona = "New York"
        elif zona_horaria == -8:
            zona = "San Francisco"
        #paso la hora a hora local de uru
        time_zone = datetime.timezone(datetime.timedelta(hours = zona_horaria))
        horageneralal = datetime.datetime.now(time_zone).time()
        hora_formateada = horageneralal.strftime(formato)
        print("La hora exacta en {} es: {}".format(zona,hora_formateada))
        imprimir_mensaje("Hora visualizada correctamente")
        input("Presione ENTER para continuar...   |")
        clear_screen()

    def fechayhorageneral():
        formato = "%B,%d,%Y %H:%M:%S"
        print()
        #paso la hora a hora local de uru
        time_zone = datetime.timezone(datetime.timedelta(hours = -3))
        fechalocal = datetime.datetime.now(time_zone)
        fecha_formateada = fechalocal.strftime(formato)
        print("La fecha y hora local es: {}".format(fecha_formateada))
        imprimir_mensaje("Hora visualizada correctamente")
        input("Presione ENTER para continuar...   |")
        clear_screen()








    while True:
            print("-----------------------------------|")
            print("-       RELOJ DEL MUNDO 1.0        |")
            print("-----------------------------------|")
            print("                                   |")
            print("1 - Visualizar hora local          |")
            print("2 - Visualizar fecha y hora local  |")
            print("3 - Visualizar hora en ny          |")
            print("4 - Visualizar hora en SF          |")
            print("0 - Salir del programa             |")
            print()
            #Controlo caracteres invalidos
            try:
                opcion = int(input(" Ingrese opcion: "))
            #Capturo el error
            except ValueError:
                print("Debes seleccionar un numero")
            else:
                if opcion == 1:
                    horageneral(-3) # le aviso que le paso como parametro -3
                elif opcion == 2:
                    fechayhorageneral()
                elif opcion == 3:
                    horageneral(-5)
                elif opcion == 4:
                    horageneral(-8)
                elif opcion == 5:
                    instruc()
                elif opcion == 0:
                    print()
                    input("Gracias por utilizar reloj del mundo, presione ENTER para salir...")
                    clear_screen()
                    break
iniciar_reloj()
