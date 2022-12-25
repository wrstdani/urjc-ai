def nVeces(x):
    dicc = {}
    for i in x:
        dicc[i] = x.count(i)

    for key, value in dicc.items():
        print('La letra', key, 'aparece', value, 'veces.')


frase = input('Introduzca una frase:')
nVeces(frase)