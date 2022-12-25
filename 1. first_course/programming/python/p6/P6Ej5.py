lista = ['1', '2', '3', '4', '5', '6', '7', '8']
lista2 = []

for i in lista:
    if lista.index(i) % 2 == 0:
        lista2.append(i)

for j in lista2:
    lista.remove(j)

print(lista)