def eliminarMultiplos(x, y):
    for i in x:
        multiplo = i * y
        if multiplo in x:
            x.remove(multiplo)
    return x

lista = list(range(1, 21))
print(lista)
listaValores = []
a = True
while a is True:
    answer = input('¿Desea eliminar múltiplos? (s/n): ')

    if answer == 'S' or answer == 's':
        numero = int(input('Introduzca un número cuyos múltiplos quiera eliminar de la lista: '))
        lista = eliminarMultiplos(lista, numero)
        print(lista)

    else:
        a = not a

