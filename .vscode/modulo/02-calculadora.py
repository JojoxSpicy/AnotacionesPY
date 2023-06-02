# llamo el archivo modulo donde se encuentran las funciones matematicas para la calculadora
import modulos

# llamo a la funcion os y luego invoco la funcion os.system('cls') para borrar la consola (similar al console.clear de c#)
# Tenga en cuenta que estas funciones solo funcionarán en la línea de comandos o en la terminal de su sistema operativo y
# no funcionarán en un IDE o entorno de desarrollo integrado como PyCharm o Spyder.
import os

# Creamos un ciclo infinito para mostrar el menú de opciones al usuario
while True:
    os.system('cls')  # para borrar la terminal como el console.clear de c#
    # Mostramos el menú de opciones al usuario
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    # Dependiendo de la opción elegida por el usuario, solicitamos los valores necesarios y realizamos la operación correspondiente
    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        # llamo la funcion sumar del archivo modulo que importe en la primera linea y lo pongo en la variable resultado
        resultado = modulos.sumar(a, b)
        print("El resultado es:", resultado)

    elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        # llamo la funcion restar del archivo modulo que importe en la primera linea y lo pongo en la variable resultado
        resultado = modulos.restar(a, b)
        print("El resultado es:", resultado)

    elif opcion == "3":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        # llamo la funcion multiplicar del archivo modulo que importe en la primera linea y lo pongo en la variable resultado
        resultado = modulos.multiplicar(a, b)
        print("El resultado es:", resultado)

    elif opcion == "4":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        resultado = modulos.dividir(a, b)
        print("El resultado es:", resultado)

    elif opcion == "5":
        print("Saliendo de la calculadora...")
        break  # Salimos del ciclo infinito

    else:
        print("Opción inválida. Intenta de nuevo.")

    # Preguntamos al usuario si desea continuar utilizando la calculadora
    while True:
        continuar = input("¿Desea continuar usando la calculadora? (s/n): ")
        if continuar.lower() == "s":
            # Salimos del ciclo interno para regresar al menú principal (ciclo principal)
            break
        elif continuar.lower() == "n":
            print("Saliendo de la calculadora...")
            exit()  # Salimos del programa
        else:
            print("Opción inválida. Intenta de nuevo.")
