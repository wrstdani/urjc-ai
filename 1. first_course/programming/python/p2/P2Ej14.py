year = int(input('Introduzca un año para comprobar si es bisiesto: '))

if year % 4 == 0 or year % 400 == 0:
    print('El año ' + str(year) + ' es bisiesto.')

else:
    print('El año' + str(year) + ' no es bisiesto.')