# Ejercicio 1

print("Ejercicio 1")
altura = int(input("Ingresa la altura del triángulo (Solo se aceptan enteros positivos): "))
if altura < 1:
    print("El número no es positivo")
else:
    for i in range(altura):
        for j in range(i+1):
            print("*", end="")
        print("") 