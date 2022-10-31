n = 1
lista = []
while n != 0:
    lista.append(n)
    n = int(input())

lista.remove(lista[0]) #utilizamos la función .remove para quitar el 1 (al principio establecimos que n = 1)
lista.sort()

for i in lista:
    print(i)
