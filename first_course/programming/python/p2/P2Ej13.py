from time import sleep

calc = input('Introduzca A/a si desea calcular la intensidad, \n B/b si desea calcular la resistencia \n o C/c si desea calcular el voltaje: ')

if calc == 'A' or calc == 'a':
    volt = float(input('Introduzca el valor del voltaje en voltios (V): '))
    res = float(input('Introduzca el valor de la resistencia en ohmios (\u03A9): '))
    inten = volt / res
    print ('El valor de la intensidad según los datos proporcionados es de ' + str(inten) +' A.')

if calc == 'B' or calc == 'b':
    volt = float(input('Introduzca el valor del voltaje en voltios (V): '))
    inten = float(input('Introduzca el valor de la intensidad en amperios (A): '))
    res = volt / inten
    print('El valor de la resistencia según los datos proporcionadoes es de ' + str(res) + ' \u03A9.')

if calc == 'C' or calc == 'c':
    inten = float(input('Introduzca el valor de la intensidad en amperios (A): '))
    res = float(input('Introduzca el valor de la resistencia en ohmios (\u03A9)'))
    volt = inten * res
    print('El valor del voltaje según los datos proporcionados es de ' + volt + ' V.')

else:
    print('No se ha introducido ninguno de los caracteres correspondientes a las opciones del programa, reiniciando...')
    sleep(3)
    exec(open("P2Ej13.py").read())