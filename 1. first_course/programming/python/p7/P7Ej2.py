def imprimir(x):
    listaElementos = []
    for i in range(len(x)):
        for j in x[i]:
            listaElementos.append(j)
    
    limite = 0
    for a in listaElementos:
        while limite != 5:
            print(a, end=' ')
            limite += 1
        print('')



def elementoMayor(x):
    listaElementos = []
    for i in range(len(x)):
        for j in x[i]:
            listaElementos.append(j)
    return max(listaElementos)

def whereIsElementoMayor(x):
    maximo = elementoMayor(x)
    for a in range(len(x)):
        for b in x[a]:
            if b == maximo:
                fila = x.index(x[a])
                columna = x[a].index(maximo)
    return 'Se encuentra en la fila %s y columna %s' % (fila + 1, columna + 1)

def nVecesMayor(x):
    listaElementos = []
    for i in range(len(x)):
        for j in x[i]:
            listaElementos.append(j)
    times = listaElementos.count(elementoMayor(x))
    if times == 1:
        return 'Solo aparece una vez'

    elif times > 1:

        return 'Aparece %s veces' % (times)
        

matriz = [
    [1, 2, 3, 4, 5],
    [2, 3, 7, 5, 9],
    [5, 4, -5, 7, 9],
    [3, 2, 1, 5, 4]
]

print('La matriz es: \n')
imprimir(matriz)
print('\n')
print('El mayor número dentro de la matriz es', elementoMayor(matriz), '.\n')
print(whereIsElementoMayor(matriz), '.\n')
print(nVecesMayor(matriz), '.')