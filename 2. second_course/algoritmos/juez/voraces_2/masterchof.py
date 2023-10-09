def isfeasible(food, nextelement, avspace):
    return avspace - food[nextelement][1] >= 0


def greedychef(food, c):
    n = len(food)
    avspace = c
    nextelement = 0
    benefit = 0
    issol = False
    while not issol and nextelement < n:
        alimento = food[nextelement]
        if isfeasible(food, nextelement, avspace):
            avspace -= alimento[1]
            benefit += alimento[2]
        else:
            valor = avspace / alimento[1]
            benefit += valor * alimento[2]
            issol = True
        nextelement += 1
    return benefit


n, c = map(int, input().strip().split())    # n: n alimentos // c: tamaño cesta
food = []
for i in range(n):
    a, t, v = map(str, input().strip().split())
    food.append((int(t)/int(v), int(t), a, i))
food.sort()
print("%.6f" % greedychef(food, c))
