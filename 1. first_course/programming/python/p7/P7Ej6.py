def inicializar():
    a = True
    filas = []
    columnas = []
    while a == True:
        cuestion = input('¿Desea introducir nodos? (s/n): ')
        if cuestion.strip() == 's' or cuestion.strip() == 'S':
            n, m = map(int, input('Introduzca un par de nodos: ').split())
            if n < 0 or m < 0 or (n < 0 and m < 0):
                a = False
            n -= 1
            m -= 1
            filas.append(n)
            columnas.append(m)
            numero_nodos = len(filas)
        else:
            a = False
    matrix = [['0'] * numero_nodos] * numero_nodos
    for i in matrix:
        for j in matrix[i]:                
            for x in filas:
                if i == x:
                    for y in columnas:
                        j = 1
    return matrix


print(inicializar())