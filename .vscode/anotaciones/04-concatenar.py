nombre = "pepe"
apellido = "gonzales"

nombre_completo = f"{nombre} {apellido}"
# se utiliza para concatenar
nombre_completo = f"{nombre[0]} {2+2}"
# pero tambien se pueden poner las expreciones que quieras
print(nombre_completo)

concatenar = f"""
hola mi nombre completo es: {nombre_completo}
"""
print(concatenar)

print("hola mi nombre completo es: " + nombre_completo)
