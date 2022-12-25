def mayus(x):
    return x.upper()

n = int(input())
lista = []

for i in range(n):
    nombre = input()
    lista.append(nombre)

for a in lista:
    print(mayus(a))