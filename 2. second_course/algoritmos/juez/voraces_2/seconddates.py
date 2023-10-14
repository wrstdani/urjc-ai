def greedydates(participantes, size):
    jovenes = []
    notanjovenes = []
    n = len(participantes)
    spaceleft = size
    nextelement = 0
    while nextelement < n:
        participante = participantes[nextelement]
        if spaceleft > 0:
            jovenes.append(participante[1])
            spaceleft -= 1
        else:
            notanjovenes.append(participante[1])
        nextelement += 1
    return jovenes, notanjovenes


n, k = map(int, input().strip().split())
participantes = []
for i in range(n):
    c, a = map(str, input().strip().split())
    participantes.append((int(a), c))
participantes.sort()
jovenes, notanjovenes = greedydates(participantes, k)
print(" ".join(jovenes), "\n", " ".join(notanjovenes))
