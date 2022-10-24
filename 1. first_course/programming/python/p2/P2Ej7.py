import math

n1 = int(input('Inserte el primer valor numérico entero:'))
n2 = int(input('Inserte el segundo valor numérico entero:'))

if n1 == (math.sqrt(n2)):
    print('El segundo es el cuadrado del primero.')

if n1 > (math.sqrt(n2)):
    print('El segundo es menor que el cuadrado del primero.')

if n1 < (math.sqrt(n2)):
    print('El segundo es mayor que el cuadrado del primero.')

