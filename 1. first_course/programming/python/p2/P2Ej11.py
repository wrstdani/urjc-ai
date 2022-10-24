encoding = 'utf-8'
caln = float(input('Introduzca su calificación numérica sobre 10: '))

if caln < 5:
    calc = 'suspenso'

if 5 <= caln < 7:
    calc = 'aprobado'

if 7 <= caln < 9:
    calc = 'notable'

if 9 <= caln < 10:
    calc = 'sobresaliente'

if caln == 10:
    calc = 'matrícula de honor'

if caln > 10:
    exec(open('P2Ej11.py').read())

    print('Usted tiene un/a ' + calc + '.')