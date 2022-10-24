c = int(input())
lista_id = []
lista_punt = []
for a in range(c):
    i, s = map(int, input().strip().split())
    lista_id.append(i)
    lista_punt.append(s)

punt_max_1 = max(lista_punt)
id_1 = map(punt_max_1, s)
lista_punt.remove(punt_max_1)
punt_max_2 = max(lista_punt)
id_2 = map(punt_max_2, s)
suma_punt_max = punt_max_1 + punt_max_2

print(map(id_1, id_2, suma_punt_max))