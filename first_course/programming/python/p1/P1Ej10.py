import math

x1 = float(input('Introduzca la coordenada x del punto 1:'))
y1 = float(input('Introduzca la coordenada y del punto 1:'))
x2 = float(input('Introduzca la coordenada x del punto 2:'))
y2 = float(input('Introduzca la coordenada y del punto 2:'))

v1 = x2 - x1
v2 = y2 - y1
dist = math.sqrt((2**v1) + (2**v2))

print('La distancia entre los dos puntos propuestos es de:', dist, 'u')