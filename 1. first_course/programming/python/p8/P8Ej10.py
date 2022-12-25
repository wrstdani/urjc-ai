def traducir(x):
    diccionario = {
        '0' : 'cero',
        '1' : 'un',
        '2' : 'dos',
        '3' : 'tres',
        '4' : 'cuatro',
        '5' : 'cinco',
        '6' : 'seis',
        '7' : 'siete',
        '8' : 'ocho',
        '9' : 'nueve'
    }

    for i in x:
        for key, value in diccionario.items():
            x.replace(key, value)

    return x


frase = input('Introduzca una frase: ')

print(traducir(frase))