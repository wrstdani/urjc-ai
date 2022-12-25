def times(x):
    dicc = {}
    lista = x.split(' ')
    for i in lista:
        dicc[i] = lista.count(i)
    for key, value in dicc.items():
        print(key, 'aparece', value, 'veces.')



frase = input('Introduzca una frase: ')
times(frase)