def primos_eratostenes(x):
    lista = list(range(2, x + 1))
    for i in lista:
        for j in range(2, x):
            if (i*j) in lista:
                lista.remove(i*j)

    return lista

limite = int(input('Introduzca un limite: '))
print(primos_eratostenes(limite))