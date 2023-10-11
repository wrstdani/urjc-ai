def isfeasible(asignaturas, nextelement, timeleft):
    return timeleft - asignaturas[nextelement][0] >= 0


def greedystudy(asignaturas, m):
    superadas = 0
    n = len(asignaturas)
    timeleft = m
    nextelement = 0
    while nextelement < n:
        asignatura = asignaturas[nextelement]
        if isfeasible(asignaturas, nextelement, timeleft):
            timeleft -= asignatura[0]
            superadas += 1
        nextelement += 1
    return superadas


n, m = map(int, input().strip().split())
asignaturas = []
for i in range(n):
    a, t = map(int, input().strip().split())
    asignaturas.append((t, a))
asignaturas.sort()
for i in range(m):
    e = int(input())
    print(greedystudy(asignaturas, e))
