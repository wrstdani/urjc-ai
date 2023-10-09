def inicializarsol(longitud):
    solinic = [0] * longitud
    return solinic


def esfactible(moneda, valores, M):
    return valores[moneda] <= M


def cambiovoraz(M, valores):
    cambio = inicializarsol(len(valores))
    moneda = 0
    while M > 0 and moneda < len(valores):
        while esfactible(moneda, valores, M):
            cambio[moneda] = cambio[moneda] + 1
            M = M - valores[moneda]
        moneda = moneda + 1

    return cambio

# PROGRAMA PRINCIPAL    
M = int(input("Introduce la cantidad a devolver en céntimos de euro: "))
valores = [200, 100, 50, 20, 10, 5, 2, 1]
cambio = cambiovoraz(M, valores)
print(cambio)
