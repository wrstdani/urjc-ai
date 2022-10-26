c = int(input())
lista_id = []
lista_punt = []
for a in range(c):
    i, s = map(int, input().strip().split())
    lista_id.append(i)
    lista_punt.append(s)

x = lista_punt.index(max(lista_punt))
max_1 = (max(lista_punt))

lista_punt_2 = (lista_punt.remove(max_1))
lista_id_2 = (lista_id.remove(lista_id[x]))

max_2 = (max(lista_punt_2))
y = lista_punt_2.index(max_2)

id_1 = (lista_id[x])
id_2 = (lista_id_2[y])

sum_max = (max_1 + max_2)

print(int(id_1), int(id_2), int(sum_max))