a, b = map(int, input().strip().split())

if a >= b:
    for i in range(a, b -1, -1):
        print(i)

else:
    for x in range(a, b + 1):
        print(x)