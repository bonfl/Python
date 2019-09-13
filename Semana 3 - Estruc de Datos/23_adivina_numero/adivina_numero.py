def clear_screen():
    import os
    os.system ("clear")
clear_screen()


import random

def jugar():
    intentos = 0
    numero_aleatorio = random.randint(1,10)

    print("Bienvenido al juego para adivinar numeros")
    print("Estoy pensando un numero del 1 al 10")
    print("Adivina cual es...")
    print("Solamente tienes 5 intentos")

    print()

    while intentos < 5:
        adivinanza = int(input("Ingrese el numero: "))

        if adivinanza == numero_aleatorio:
            print("Adivinaste!!!")
            jugar_nuevamente = input("Jugar de nuevo? si/no: ")
            if jugar_nuevamente.lower() == "si":
                jugar()
            else:
                break

        elif numero_aleatorio > adivinanza:
            print("Fallaste, el numero es mayor")

        else:
            print("Fallaste, el numero es menor")

        intentos += 1
        print("Intento {}/5".format(intentos))
    else:
        print("Gracias x jugar")
        jugar_nuevamente = input("Jugar de nuevo? si/no: ")
        if jugar_nuevamente.lower() == "si":
            jugar()

jugar()
