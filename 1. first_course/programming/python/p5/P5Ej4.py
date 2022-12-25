def ahorcado(x, y):
    limiteFallos = 4
    nFallos = 0
    solucion = y

    while nFallos != limiteFallos and solucion != x:
        proposicion = input('Jugador A, introduce una letra: \n')

        while len(proposicion.split()) > 1:
            proposicion = input('La entrada ha de ser una única letra: ')
        if proposicion in x:
            solucion = y.replace(y[x.index(proposicion)], proposicion)
            print((solucion), proposicion)
        else:
            nFallos += 1
            print('El Jugador A ha fallado. Le quedan', 5 - nFallos,'intentos.')

    if nFallos != limiteFallos:
        return 'El jugador B ha ganado'

    elif solucion == x:
        return 'El jugador A ha ganado'


print('Juego del ahorcado \n')
cadena1 = input('Palabra del Jugador B: \n')
print('La palabra del Jugador B tiene', len(cadena1), 'letras. \n')
cadena2 = input('Para inicializar el juego, la entrada ha de tener la misma longitud que la del Jugador B y ha de estar rellena con * o _. \n')

while len(cadena1.split()) != len(cadena2.split()) or '*' not in cadena2:
    print('La palabra del Jugador B tiene', len(cadena1), 'letras. \n')
    cadena2 = input('Para inicializar el juego, la entrada ha de tener la misma longitud que la del Jugador B y ha de estar rellena con * o _. \n')

print(ahorcado(cadena1, cadena2))