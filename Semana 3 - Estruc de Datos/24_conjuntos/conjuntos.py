def clear_screen():
    import os
    os.system ("clear")
clear_screen()


print("-----------------------------------|")
print("-         CONJUNTOS   1.0          |")
print("-----------------------------------|")
print()
print()
print("Bienvenido al programa de conjuntos")
print("Introduce los elementos del conjunto separados por espacios")
print("Ejemplo: 1 2 3 4 5 6")

conjunto_a = set(input("Conjunto A: ").split())

conjunto_b = set(input("Conjunto B: ").split())

print()
print(conjunto_a)
print(conjunto_b)
print()
print("Gracias")
