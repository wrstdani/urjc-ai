def cuadrado(x):
    lista_c = []
    for i in x:
        i = i**2
        lista_c.append(i)
    return lista_c
        

lista = list(range(1,4))

print(lista, cuadrado(lista))