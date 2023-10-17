def isfeasible(casos, nextelement, moneyav):
    return moneyav - casos[nextelement][1] >= 0


def greedycherlo(casos, maxmoney):
    n = len(casos)
    beneficio = 0
    lcasos = []
    nextelement = 0
    issol = False
    moneyav = maxmoney
    while not issol and nextelement < n:
        caso = casos[nextelement]
        if isfeasible(casos, nextelement, moneyav):
            moneyav -= caso[1]
            beneficio += caso[2]
            lcasos.append(caso[3])
        else:
            valor = moneyav / caso[1]
            beneficio += valor * caso[2]
            lcasos.append(caso[3])
            issol = True
        nextelement += 1
    return sorted(lcasos), round(beneficio)

n, m = map(int, input().strip().split())
casos = []
for i in range(n):
    p, d = map(int, input().strip().split())
    casos.append((d/p, p, d, i))
casos.sort(reverse=True)
lcasos, dinero = greedycherlo(casos, m)
lcasos = [str(caso) for caso in lcasos]
print(" ".join(lcasos), "\n", dinero)
