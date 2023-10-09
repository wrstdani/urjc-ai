def tpacientes(npacientes):
    dtiempos = {}
    for i in range(npacientes):
        dtiempos["p%d" % (i + 1)] = int(input("Introduce el tiempo de p%d: " % (i + 1)))
    return dtiempos


def ordtiempos(npacientes, dtiempos):
    lfin = [0] * npacientes
    for i in range(npacientes):
        for key, value in dtiempos:
            lfin[i] = dtiempos[min(dtiempos.values())]


# PROGRAMA PRINCIPAL
npacientes = int(input("Introduce el número de pacientes: "))
print(tpacientes(npacientes).values())
