from time import sleep

num = int(input('Introduzca un número cualquiera mayor que 2:'))

if num > 2:
    lista = range(2, num)
    for i in lista:
        if i % 2 == 0:
            print(str(i)).pop(2)
            
else:
    print('El número introducido es menor que 2, reiniciando programa...')
    sleep(3)
    exec(open("P3Ej3.py").read())