def insertar(x):
    elemento = int(input('Introduzca un elemento: '))
    x.append(elemento)
    return x

def eliminar(x):
    elemento = int(input('Introduzca un elemento para eliminar: '))
    x.remove(elemento)
    return x

def ocurrencias(x):
    contador = 0
    elemento = int(input('Introduzca un elemento: '))
    for i in x:
        if i == elemento:
            contador += 1
    return contador


lista = [1, 1, 3, 4, 2, 2, 5, 6, 5, 7, 10, 23]

print(insertar(lista), '\n')

print(eliminar(lista), '\n')

print(ocurrencias(lista), '\n')
