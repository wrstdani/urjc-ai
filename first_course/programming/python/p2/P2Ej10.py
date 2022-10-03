a = float(input('Introduzca el primer valor (a): '))
b = float(input('Introduzca el segundo valor (b): '))
c = float(input('Introduzca el tercer valor (c): '))
d = float(input('Introduzca el cuarto valor (d): '))
e = float(input('Introduzca el quinto valor (e): '))

if (((a - b) * (a - b)) < ((a - c) * (a - c))):
    closest = b
else:
    closest = c

if (((a - closest) * (a - closest)) > ((a - d) * (a - d))):
    closest = d

if (((a - closest) * (a - closest)) > ((a - e) * (a - e))):
    closest = e

print('El valor más cercano a ' + str(a) + ' es ' + str(closest))