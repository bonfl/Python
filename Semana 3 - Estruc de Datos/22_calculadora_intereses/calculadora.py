def clear_screen():
    import os
    os.system ("clear")
clear_screen()


#EJEMPLO               xxxxx          yyyy           zzzz        rrrr
#Para 1 día:       108.184.75.- * ( ( 1,1709 ) ˆ ( 1 / 365 ))   - 1 ) =      46,77.-
def tea():
    k = float(input("Ingrese Capital: "))
    t = float(input("Ingrese Tasa de Interes: "))
    p = int(input("Ingrese Plazo en dias: "))

    #Calculo exponencial
    intereses = k*((((t+100)/100)**(p/365)) -1)
    print ("Intereses a ",p,"dias:  ", round(intereses,2))
    print ("Capital + Intereses:  ", round(k + intereses,2))


def iniciar_calculadora():
    print("-----------------------------------|")
    print("-         CALCULADORA 1.0          |")
    print("-----------------------------------|")


while True:
    print("                                   |")
    print("1 - Tasa Lineal Anual              |")
    print("2 - Tasa Lineal Mensual            |")
    print("3 - Tasa Efectiva Mensual          |")
    print("4 - Tasa Efectiva Anual            |")
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
            tla()
        elif opcion == 2:
            tlm()
        elif opcion == 3:
            tem()
        elif opcion == 4:
            tea()

        elif opcion == 0:
            break


iniciar_calculadora()
