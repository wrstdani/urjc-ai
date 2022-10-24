import math

a = float(input('Introduzca el valor del lado 1:'))
b = float(input('Introduzca el valor del lado 2:'))
c = float(input('Introduzca el valor del lado 3:'))

s = (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print('El área del triángulo es de:', area, 'm^2')