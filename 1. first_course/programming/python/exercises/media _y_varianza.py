num_notas = int(input('Introduzca el número de notas: '))

media = 0

x = []

for i in range(num_notas):
    temp = float(input('Valor' + str(i + 1) + ':'))
    x.append(temp)
    media = media + temp    

media = media / num_notas
varianza = ((2** (temp-media)) / num_notas)
print('La media de sus calificaciones es de: ' + str(media) + '\n y la varianza es de: ' + str(varianza) + '.')