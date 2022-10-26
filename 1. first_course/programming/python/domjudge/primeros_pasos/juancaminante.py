n = int(input())
m = int(input())

if 1 <= n <= 10000 and 1 <= m <= 10000:
    #convertimos unidades de longitud de zancada
    resultado = n * m
    resultado_metros = (resultado / 1000)
    print(resultado_metros)