def isfeasible(almendras, nextCandIdx, freeWeight):
    return freeWeight - almendras[nextCandIdx][2] >= 0


def greedyknapsack(almendras, maxWeight):
    n = len(almendras)
    freeWeight = maxWeight
    isSol = False
    nextCandIdx = 0
    nutrition = 0
    while not isSol and nextCandIdx < n:
        almendra = almendras[nextCandIdx]
        if isfeasible(almendras, nextCandIdx, freeWeight):
            freeWeight -= almendra[2]  # en una tupla se accede a las posiciones igual que en una lista
            nutrition += almendra[1]
        else:
            valor = freeWeight / almendra[2]
            nutrition += valor * almendra[1]
            isSol = True
        nextCandIdx += 1
    return nutrition


n, m = map(int, input().strip().split())
almendras = []
for i in range(n):
    v, p = map(int, input().strip().split())
    almendras.append((v/p, v, p, i))
almendras.sort(reverse=True)

for i in range(m):
    mv, mp = map(int, input().strip().split())
    nutVal = greedyknapsack(almendras, mp)
    if nutVal >= mv:
        print("PUEDE")
    else:
        print("TOS")
