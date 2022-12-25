def inicializar(nFilas, nColumnas):
    fila = [0] * nColumnas
    tablero = []
    for i in range(nFilas):
        tablero.append(fila[:])
    return tablero


def imprimirV1(tablero):
    for i in range(len(tablero)):
        print(tablero[i])


def imprimirV2(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end = ' ')
        print('')


def fill(tablero, fila, columnaInicio, elemento):
    for col in range(columnaInicio,len(tablero[fila]),2):
        tablero[fila][col] = elemento
    return tablero


def fillV2(tablero):
    for fila in range(len(tablero)):
        for col in range(len(tablero[fila])):
            if (fila + col) % 2 == 0:
                if fila < 3:
                    tablero[fila][col] = 1

                elif fila > 4:
                    tablero[fila][col] = 2
    return tablero

tablero = inicializar(8,8)

tablero = fillV2(tablero)
imprimirV2(tablero)