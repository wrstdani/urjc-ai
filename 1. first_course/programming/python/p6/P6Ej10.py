frase = input('Introduzca la frase: ')
vocales = 'aeiou'
listaVocales = []
listaConsonantes = []

for i in vocales:
    if i in frase:
        listaVocales.append(i)

for j in frase:
    if j not in vocales and j is not ' ':
        listaConsonantes.append(j)

print(listaVocales)
print(listaConsonantes)