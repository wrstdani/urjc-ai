import math

side1 = float(input('Introduzca el valor del lado 1 en metros:'))
side2 = float(input('Introduzca el valor del lado 2 en metros:'))
angle = float(input('Introduzca el valor del ángulo \u03B8 en grados:'))

area = (1/2) * side1 * side2 * math.sin(angle * math.pi / 180)

print('Siendo de', side1, 'm el lado 1, de', side2, 'el lado 2 y de', angle, 'grados el ángulo, el área del triángulo es de', area, 'm^2')