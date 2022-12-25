def contarPalabrasEnk(x, y):
    nEspacios = 0
    for i in range(x):
        if y[i] == ' ':
            nEspacios += 1
    return nEspacios + 1


k = int(input())
cadena = input()

print('En una longitud', k, 'en la cadena hay', contarPalabrasEnk(k, cadena), 'palabras.')
