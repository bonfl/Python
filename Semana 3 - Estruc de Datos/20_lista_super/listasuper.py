def clear_screen():
    import os
    os.system ("clear")
clear_screen()

listasup1 = []

def funagregar():
    print
    articulo = input("Ingrese articulo a Agregar: ")
    listasup1.append(articulo.capitalize())
    print(listasup1)

def funlistar():
    for articulo in listasup1:
        print(articulo)

def funborrar():
  print
  articulo = input("Ingrese articulo a Borrar: ")
  listasup1.remove(articulo.capitalize())
  print(listasup1)


while True:
    print("-------------------------------------------------")
    print("---------------LISTASUPER---2.0------------------")
    print("-------------------------------------------------")
    print
    print("Bienvenidos a la lista para supermercados 2.0")
    print
    print("1 - Agregar a la lista")
    print("2 - Borrar de la lista")
    print("3 - Visualizar lista")
    print("0 - Salir")
    opcion = int(input("Ingrese opcion deseada: "))

    if opcion == 1:
        funagregar()
    elif opcion == 2:
        funborrar()
    elif opcion == 3:
      print()
      print()
      print()
      funlistar()
      print()
      print()
    elif opcion == 0:
        clear_screen()
        break

    else:
        #print("Opcion invalida, reintente nuevamente")
        clear_screen()
