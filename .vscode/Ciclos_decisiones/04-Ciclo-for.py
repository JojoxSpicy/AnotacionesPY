# Imprimir los elementos de una lista utilizando un ciclo for

# Creamos una lista de nombres
nombres = ["Juan", "María", "Pedro", "Ana"]

# Usamos un ciclo for para imprimir cada nombre en la lista
for nombre in nombres:
    print(nombre)

# La ejecución continúa aquí después de que el ciclo termina
print("Terminado")

# ==========================================================================================================================
# ==========================================================================================================================

# Inicializamos el contador a cero
count = 0

# Recorremos los números del 1 al 100
for i in range(1, 101):
    # Convertimos el número a una cadena de caracteres para poder buscar el "9"
    str_i = str(i)

    # Si el número contiene un "9", incrementamos el contador
    if "9" in str_i:
        count += 1

# Mostramos el resultado
print("Hay", count, "números '9' del 1 al 100 sin separar el 99 ")
