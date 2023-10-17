def greedystudy(asignaturas, maxtime):
    n = len(asignaturas)
    nextelement = 0
    tiempo = 0
    ltiempos = []
    while nextelement < n:
        tasignatura = asignaturas[nextelement][0]
        tiempo += tasignatura
        ltiempos.append(tiempo)
        nextelement += 1
    return maxtime >= sum(ltiempos)


n, m = map(int, input().strip().split())
asignaturas = []
for i in range(n):
    a, t = map(int, input().strip().split())
    asignaturas.append((t, a))
asignaturas.sort()
for i in range(m):
    e = int(input())
    if greedystudy(asignaturas, e):
        print("APROBADO")
    else:
        print("SUSPENSO")
