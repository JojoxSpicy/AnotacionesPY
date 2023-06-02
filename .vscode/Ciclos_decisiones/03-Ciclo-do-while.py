# Adivinar un número secreto utilizando un ciclo do-while simulado (ya que el lenguaje Py no tiene este ciclo como tal)

import random

# Generamos un número aleatorio entre 1 y 100
secreto = random.randint(1, 100)

# Creamos un ciclo do-while simulado para permitir múltiples intentos
while True:
    # Pedimos al usuario que adivine el número
    guess = int(input("Adivina el número secreto (entre 1 y 100): "))

    # Comparamos la conjetura con el número secreto
    if guess == secreto:
        print("¡Correcto! ¡Lo adivinaste!")
        break
    elif guess < secreto:
        print("Demasiado bajo. Intenta otra vez.")
    else:
        print("Demasiado alto. Intenta otra vez.")
