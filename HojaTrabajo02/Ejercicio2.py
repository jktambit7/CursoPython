# Ejercicio 2
print("Ejercicio 2")
print("===========")
print("")

num = int(input("Ingrese un número entero positivo: "))
n =  num
if num < 0:
    print("El número no es positivo")
else:
    for x in range(num+1):
        print(n, end = ", ")
        n = n - 1
