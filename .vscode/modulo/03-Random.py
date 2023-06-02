import random

# Lista de nombres
nombres = ['Rojo', 'Amarillo', 'Verde',
           'Dorado', 'Azul', 'Negro']

# Elegir un nombre al azar
nombre_elegido = random.choice(nombres)
# (random.choice) selecciona un nombre random de la lista nombres

# Imprimir el nombre elegido
print(f"El nombre elegido es: {nombre_elegido}")
