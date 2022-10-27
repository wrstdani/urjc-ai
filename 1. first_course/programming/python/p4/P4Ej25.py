n = str(input())

def sumaCifrasR(n):
    if len(n) == 1:
        return int(n)
    else:
        return int(n[0]) + sumaCifrasR(n[1:])

def sumaCifrasI(n):
    suma = 0
    for i in n:
        suma += int(i)
    return suma

print(sumaCifrasR(n))
print(sumaCifrasI(n))