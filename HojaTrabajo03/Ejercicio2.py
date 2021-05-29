#Ejercicio 2
nombre = input("¿Cuál es su nombre? ")
genero = input("¿Cuál es su sexo? (M o H) ")

nombre = nombre.lower()

if genero == "M":
    if nombre < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre > "n":
        grupo = "A"
    else:
        grupo = "B"

print("Su grupo es el " + grupo)