def conjuntoLetras(x):
    lista = []
    for i in x:
        if i not in lista:
            lista.append(i)
    return lista

def letrasEn1NoEn2(x, y):
    lista = []
    for i in x:
        if i not in y and i not in lista:
            lista.append(i)
    return lista

def totalLetras(x, y):
    lista = []
    for i in x:
        if i not in lista:
            lista.append(i)
    for j in y:
        if j not in lista:
            lista.append(j)
    return lista

def letrasComunes(x, y):
    lista = []
    for i in x:
        if i in y and i not in lista:
            lista.append(i)
    return lista

palabra1 = input('Introduzca una palabra: ')
print(conjuntoLetras(palabra1))

palabra2 = input('Introduzca otra palabra: ')
print(conjuntoLetras(palabra2))

print('Las letras que están en', palabra1, 'y no en', palabra2, 'son:', letrasEn1NoEn2(palabra1, palabra2))
print('Las letras que están en', palabra2, 'y no en', palabra1, 'son:', letrasEn1NoEn2(palabra2, palabra1))

print('La totalidad de las letras:', totalLetras(palabra1, palabra2))

print('Las letras comunes:', letrasComunes(palabra1, palabra2))