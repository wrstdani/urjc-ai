def invertir(x):
    lista_f = list(reversed(x))
    return lista_f

def invertir_2(z):
    lista2 = []
    for i in range(len(z) - 1, -1, -1):
        lista2.append(z[i])
    return lista2

def invertir_3(y):
    lista2 = [0] * len(y)
    for i in range(len(y)):
        lista2[i] = y[len(y) -1 -i]
    return lista2

def invertir_4(b):
    lista2 = []
    for i in range(len(b)):
        lista2 = [b[i]] + lista2
    return lista2



a = [1, 2, 4, 5, 6, 9, 3]
print('Este programa imprime la lista inversa de otra lista. \n')
print('Esta es la lista predefinida:', a, '\n')
print('Método 1:', invertir(a), '\n')
print('Método 2:', invertir_2(a), '\n')
print('Método 3:', invertir_3(a), '\n')
print('Método 4:', invertir_4(a))