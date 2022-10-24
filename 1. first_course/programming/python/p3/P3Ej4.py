num_valores = int(input('Introduzca el número de valores deseado: '))

lista = []

for i in range(num_valores):
    val = int(input('Introduzca el valor de v' + str(i +1 ) + ': '))
    lista.append(val)

print(lista)

if lista != 0:
    print('El valor mínimo es ' + str(min(lista)))

else:
    print('El valor mínimo es 0.')