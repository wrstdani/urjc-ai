num_terminos = int(input())
val_x = float(input())
lista = []
resultado_fact = 1

for i in range(num_terminos + 1):
    n = (2 * i + 1)
    if n == 0 or n == 1:
        resultado_fact = 1
    else:
        for a in range(1, n + 1):
            lista.append(i)
        for x in lista:
            resultado_fact = resultado_fact * x
    seno = (((-1)**i) * (((val_x)**n)/(resultado_fact)))
print(float(seno))




