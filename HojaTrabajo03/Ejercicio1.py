#Ejercicio 1

contraseña = input("Ingrese una contraseña a ser guardada:  ")
solicitud_contraseña = input("Ingrese nuevamente la contraseña:   ")

contraseña = contraseña.lower()
solicitud_contraseña = solicitud_contraseña.lower()

if contraseña == solicitud_contraseña:
    print("La contraseña si coincide con la guardada")
else:
    print("La contraseña no coincide con la guardada")