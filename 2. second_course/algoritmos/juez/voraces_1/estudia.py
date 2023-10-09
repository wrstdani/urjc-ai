def isfeasible(asignaturas, nextelement, avtime):
    return avtime - asignaturas[nextelement][0] >= 0


def greedystudy(asignaturas, maxtiempo):
    aprobadas = 0
    issol = False
    n = len(asignaturas)
    nextelement = 0
    avtime = maxtiempo
    while not issol and nextelement < n:
        asignatura = asignaturas[nextelement]
        if isfeasible(asignaturas, nextelement, avtime):
            avtime -= asignatura[0]
            aprobadas += 1
        else:
            issol = True
        nextelement += 1
    return aprobadas



n, m = map(int, input().strip().split())
asignaturas = []
for i in range(n):
    a, t = map(int, input().strip().split())
    asignaturas.append((t, a))
asignaturas.sort()

for i in range(m):
    e = int(input())
    print(greedystudy(asignaturas, e))
