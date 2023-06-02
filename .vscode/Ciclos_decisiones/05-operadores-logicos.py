# and, or, not

# (and) se utiliza cuando tenemos 2 condiciones y ambas son verdaderas

# (or) se utiliza cuando tenemos 2 condiciones pero no importa si una es verdadera y otra falsa o viceversa

# (not) se utiliza para negar una condicion


edad = 18

encendido = True

dañado = False

licencia = False

sabe_manejar = True

# en este ejemplo decimos que si el carro no esta dañado  y esta encendido y eres mayor de 17
# y tienes licencia o sabes manejar pues: puedes conducir el vehiculo.
if not dañado and encendido and edad > 17 and licencia or sabe_manejar:
    print("puedes conducir el vehiculo")
# estas operaciones se leen de izquierda a derecha siempre pero si queremos que algo se lea primero le podemos poner
# parentesis
