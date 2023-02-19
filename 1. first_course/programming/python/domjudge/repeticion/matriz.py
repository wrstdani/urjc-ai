dimension = int(input())
nVeces = 0

if dimension > 1:
   for i in range(1, (dimension ** 2) + 1):
    print(i, end=' ')
    nVeces += 1
    if nVeces == dimension:
        print('')
        nVeces = 0