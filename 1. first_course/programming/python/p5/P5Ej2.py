def contarPalabras(x):
    nEspacios = 0
    for i in x:
        if i == ' ':
            nEspacios += 1
    return nEspacios + 1


frase = input('Introduzca una frase para contar sus palabras: ')

print('La frase tiene', contarPalabras(frase), 'palabras.')