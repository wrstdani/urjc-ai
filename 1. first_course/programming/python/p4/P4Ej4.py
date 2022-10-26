a, b, i = map(int, input().strip().split())

def sumatorio(a, b):
    if a > b:
        return 0
    elif a <= b:
        for n in range(i):
            while n <= b:
                n += 1
        return n

print(sumatorio(a, b))