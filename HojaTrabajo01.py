peso = input("¿Cuál es su peso expresado en kg?  ")
estatura = input("¿Cuál es su estatura expresada en metros?  ")

imc = round(float(peso) / float(estatura)**2,2)
print("Su indice de masa corporal (imc) es: ")
print(imc)