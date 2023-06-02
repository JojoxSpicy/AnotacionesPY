# vamos a simular que vas a entrar al cine y que si eres mayor que 57 tienes un descuento
# si eres mayor de 18 entras y si eres menor un mensaje de (lo siento no puedes pasar)


num1 = int(input("Ingrese su edad: "))


if num1 >= 57:  # aqui lo que desimos es que si numero es mayor o igual a 57
    # se imprime este mensaje (se deja un espacio en [tab] para que sean considerados dentro del if)
    print("Puede entrar con descuento")
elif num1 > 17:  # aqui desimos sino si num1 es mayor que 17
    print("puede entrar")  # se imprime esto
else:  # (else) corre el siguiente mensaje si no es ninguna de las anteriores
    print("lo siento no puedes pasar")


# operador ternario

edad = 18
mensaje = "es mayor" if edad > 17 else "es menor"

print(mensaje)
