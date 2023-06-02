descripcion = """aqui anotare todo lo que aparece en el 
video de hola mundo con respecto a los strings"""

print(len(descripcion))
# (funcion len) se utiliza para que te diga cuantos caracteres tiene una variable
print(descripcion[0])
# se utiliza en este caso para obtener el primer digito/letra de la variable porque la
# posicion es 0
print(descripcion[0:4])
# se utiliza en este caso para que me entregue la palabra "aqui" que empieza en el 0 y termina en el 4
print(descripcion.capitalize())
# (funcion capitalize) pone la primera letra del string mayuscula y las demas minusculas
print(descripcion.upper())
# (funcion upper) pone todas las letras mayusculas
print(descripcion.lower())
# (funcion lower) pone todas las letras en minusculas
print(descripcion.title())
# (funcion title) pone la primera letra de cada palabra en mayuscula y las demas minuscula
print(descripcion.strip())
# (funcion strip) quita todos los espacios en blanco que queden a la izquierda y a la derecha del string
# mejor usar antes del capitalize por seguridad ejem:
print(descripcion.strip().capitalize())
# se pueden encadenar las funciones
# tambien tenermos "lstrip" que quita los espacios solo de la izquierda y "rstrip" que los quita de la derecha
print(descripcion.find("mundo"))
# (funcion find) se utiliza para buscar una letra/numero o palabra en especifica dentro de un string  y te da el indice
# o posicion del mismo (si te da un numero negativo es porque no lo encuentra o mejor dicho no existe)
print(descripcion.replace("aqui", "ahi"))
# (funcion replace) sirve para remplazar se pone el que quieres remplazar primero luego el reemplazo
print("asi" in descripcion)
# esta funcion solo te dice en este caso si "asi" se encuentra en la variable descripcion (dice si es true o false)
print("exp" not in descripcion)
# esta te dice si no se encuentra en este caso "exp" dentro de descripcion
