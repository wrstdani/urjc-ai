val = float(input('Introduzca un valor positivo para agregar a la lista o negativo para dejar de añadir valores a ella: '))
lista = []
media = 0

while val >= 0:
    if val >= 0:
        lista.append(val)
        media = media + val
        val = float(input('Introduzca un valor: '))
    
    else:
        print('Reiniciando programa...')
        exec(open('P3Ej5.py').read())


media = media / len(lista)
print(str(media))
