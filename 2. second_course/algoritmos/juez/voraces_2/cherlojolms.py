def isfeasible(casos, avmoney, nextelement):
    return avmoney - casos[nextelement][1] >= 0


def greedycherlo(casos, maxmoney):
    beneficio = 0
    resueltos = []
    n = len(casos)
    avmoney = maxmoney
    nextelement = 0
    issol = False
    while not issol and nextelement < n:
        caso = casos[nextelement]
        if isfeasible(casos, avmoney, nextelement):
            resueltos.append(caso[3])
            beneficio += caso[2]
            avmoney -= caso[1]
        else:
            valor = avmoney / caso[1]
            beneficio += valor * caso[2]
            resueltos.append(caso[3])
            issol = True
        nextelement += 1
    resueltos = [str(num) for num in sorted(resueltos)]
    return resueltos, beneficio


n, m = map(int, input().strip().split())
casos = []
for i in range(n):
    p, d = map(int, input().strip().split())
    casos.append((p/d, p, d, i))
casos.sort()
resueltos, btotal = greedycherlo(casos, m)
print(resueltos)
print(round(btotal))
