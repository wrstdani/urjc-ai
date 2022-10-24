import os
import time
from math import sqrt

print('Con este programa resolveremos una ecuación de segundo grado del estilo ax^2 + bx + x = 0')
time.sleep(2)

a = int(input('Introduce el valor a entero:'))
b = int(input('Introduce el valor b entero:'))
c = int(input('Introduce el valor c entero:'))

if (a == 0): 
    if (b != 0):
        print('Al ser a = 0, la ecuación sería de primer grado y, por tanto, x = ' + str(-c / b))
    
    else:
        if (c != 0):
            print('La ecuación no tiene solución dentro del conjunto de los números reales.')

        else:
            print('La ecuación tiene infinitas soluciones.')
    
else:
    if((2 ** b) - 4 * a * c < 0):
        print('La ecuación no tiene solución dentro del conjunto de los números reales.')
    
    else:
        if((2 ** b) - 4 * a * c >= 0):
            ec_1 = ((-b - sqrt((2 ** b) - 4 * a * c)) / (2 * a))
            ec_2 = ((-b + sqrt((2 ** b) - 4 * a * c)) / (2 * a))
            print('La primera solución x1 es: ' + str(ec_1) + '\n y la segunda solución es: ' + str(ec_2))
