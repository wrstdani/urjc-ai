# Pedimos el número al usuario
n = int(input())
nVeces = 0
limite = 1

for i in range(1, n + 1):
    print(i, end='')
    nVeces += 1
    if nVeces == limite:
        print('')
        limite += 1
        nVeces = 0