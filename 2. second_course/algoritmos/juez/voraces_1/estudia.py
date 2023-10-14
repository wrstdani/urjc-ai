def isfeasible(asignaturas, nextelement, timeleft):
    return timeleft - asignaturas[nextelement][0] >= 0


def greedystudy(asignaturas, maxtime):
    n = len(asignaturas)
    timeleft = maxtime
    nextelement = 0
    while nextelement < n:
        asignatura = asignaturas[nextelement]
        if not isfeasible(asignaturas, nextelement, timeleft):
            return False
        else: 
            timeleft -= asignatura[0]
        nextelement += 1
    return True


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
