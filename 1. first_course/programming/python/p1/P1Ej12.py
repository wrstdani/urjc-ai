frase = str(input('Introduzca la frase cuyos dígitos desea convertir a letras:'))

sustituyentes = {
    '0': 'cero',
    '1': 'uno',
    '2': 'dos',
    '3': 'tres',
    '4': 'cuatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'siete',
    '8': 'ocho',
    '9': 'nueve'
}

for key, value in sustituyentes.items():
    frase = frase.replace(key, value)

print(frase)