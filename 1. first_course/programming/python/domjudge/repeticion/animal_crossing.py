c = int(input())
lista_id = []
lista_punt = []
for a in range(c):
    i, s = map(int, input().strip().split())
    lista_id.append(i)
    lista_punt.append(s)

punt_max_1 = max(lista_punt)
x = lista_punt.index(punt_max_1)

lista_punt[x] = 0

punt_max_2 = max(lista_punt) 
y = lista_punt.index(punt_max_2)

id_1 = lista_id[x]
id_2 = lista_id[y]
suma_punt_max = punt_max_1 + punt_max_2

print(id_1, id_2, suma_punt_max)