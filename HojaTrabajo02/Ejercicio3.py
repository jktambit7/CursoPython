# Ejercicio 3
n = int (input("Ingresa un número entero positivo mayor que 2: "))

i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es número primo ")
else:
    print(str(n) + " no es número primo")