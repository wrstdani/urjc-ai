import random

n = int(input('Introduzca el último valor que desea incuir en el rango de los números posibles para el juego: '))

num = random.randrange(1, (n + 1))

val = int(input('Introduzca su intento:'))

while val != num:
    val = int(input('Introduzca su intento:'))

if val == num:
    print('Ha acertado.')