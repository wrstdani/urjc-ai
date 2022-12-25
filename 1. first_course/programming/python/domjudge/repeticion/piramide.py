n = int(input())
nVeces = 1

for i in range(1, n + 1):
    for j in range(nVeces):
        print('*', end='')
    print('')
    nVeces += 1