from math import sqrt

print('Programa que calcula la raíz cuadrada de un número positivo')
num = float(input('Introduzca un número positivo para calcular su raíz cuadrada: '))

while num < 0:
    num = float(input('Por favor, asegúrese de que el valor es mayor que 0: '))

print('La raíz cuadrada de ' + str(num) + ' es ' + str(sqrt(num)))

