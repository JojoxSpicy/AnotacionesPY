import math  # accede a la libreria math la cual tiene funciones matematicas


imaginario = 2+2j
# 2+2i (i es la raiz cuadrada de menos uno en matematicas no existe ningun numero multiplicado por si mismo
# da menos 1 por eso es un numero imaginario) y se representa con la j en Py

print(1+1)
print(2-2)
print(5*5)
print(10/5)  # division que entrega los decimales
print(10//5)  # division que entrega los enteros
print(3 % 2)  # (%) modulo entrega el valor restante de la division
print(2 ** 3)  # (**) se utiliza para elevar a la potencia

print(round(1.3))
# (round) nos dice a cual numero entero esta mas cercano el valor ingresado
print(abs(-55))
# (abs)entrega el valor absoluto (saca el signo de la ecuacion sea positivo o negativo)

# ALGUNAS DE LAS FUNCIONES MAS IMPORTANTES DE MATH LAS DEMAS SE ENCUENTRAN EN:
# https://docs.python.org/3/library/math.html

print(math.ceil(1.1))
# (ceil) lleva el numero al numero superior entero mas cercano
print(math.floor(1.9999))
# (floor) lleva el numero al numero inferior entero mas cercano
print(math.pow(10, 3))
# (pow) eleva el numero de la izquierda al valor de la derecha
print(math.sqrt(9))
# (sqrt) saca la raiz cuadrada
