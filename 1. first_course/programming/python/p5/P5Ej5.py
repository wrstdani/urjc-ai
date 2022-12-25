def comprobar(x):
    for i in x.strip():
        if i not in listaCaracteres:
            return 'La fórmula %s no es correcta.' % (x)
    return 'La fórmula %s es correcta.' % (x)

def numeroAtomos(x):
    atC = []
    atH = []
    atO = []
    atN = []

    for i in x:
        if i == 'C':
            if x[x.index('C') + 1] in listaCaracteres:
                atC.append(int(x[x.index('C') + 1]))
            else:
                atC.append(1)

    return atC

#def pesosAtomicos(x):

    


listaCaracteres = ['C', 'H', 'O', 'N', '2', '3', '4', '5', '6']

formula = input('Introduzca una fórmula química: ')
print(comprobar(formula), '\n')
print(numeroAtomos(formula), '\n')