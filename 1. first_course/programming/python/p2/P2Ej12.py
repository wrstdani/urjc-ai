######################################################Calculadora##############################################################
from time import sleep

operando_1 = float(input('Introduzca el primer operando: '))
operando_2 = float(input('Introduzca el segundo operando: '))

operacion = input('Pulse 1 para sumarlos, 2 para restarlos, 3 para multiplicarlos o 4 para dividirlos: ')

# Suma
if operacion == '1':
    suma = operando_1 + operando_2
    print('El resultado de la suma es: ' + str(suma))

if operacion == '2':
    resta = operando_1 - operando_2
    if resta < 0:
        resultado_negativo = (input('La resta resulta en un número negativo. ¿Desea invertir el orden de los operandos? (y/n): '))
        if resultado_negativo == 'y':
            resta = operando_2 - operando_1
            print('El resultado de la resta es: ' + str(resta))
        elif resultado_negativo == 'n':
            print('El resultado de la resta es: ' + str(resta))
        else:
            print('Ha introducido un caracter no admitido, el programa se reiniciará automáticamente.')
            sleep(3)
            exec(open("P2Ej12.py").read())
    else:
        print('El resultado de la resta es: ' + str(resta))

if operacion == '3': 
    mult = operando_1 * operando_2
    print('El resultado de la multiplicación es: ' + str(mult))

if operacion == '4':
    div = operando_1 / operando_2
    print('El resultado de la división es: ' + str(div))

else: 
    print('Ha introducido un caracter no admitido, el programa se reiniciará automáticamente.')
    sleep(3)
    exec(open("P2Ej12.py").read())