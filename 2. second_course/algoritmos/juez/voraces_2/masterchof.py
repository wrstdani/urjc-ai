def isfeasible(alimentos, nextelement, spaceav):
    return spaceav - alimentos[nextelement][1] >= 0

def greedychef(alimentos, maxspace):
    n = len(alimentos)
    spaceav = maxspace
    nextelement = 0
    issol = False
    beneficio = 0
    while not issol and nextelement < n:
        alimento = alimentos[nextelement]
        if isfeasible(alimentos, nextelement, spaceav):
            spaceav -= alimento[1]
            beneficio += alimento[2]
        else:
            valor = spaceav / alimento[1]
            beneficio += valor * alimento[2]
            issol = True
        nextelement += 1
    return beneficio

n, c = map(int, input().strip().split())
alimentos = []
for i in range(n):
    a, t, v = map(str, input().strip().split())
    alimentos.append((int(v)/int(t), int(t), int(v), a))
alimentos.sort(reverse=True)
print("%.6f" % greedychef(alimentos, c))
