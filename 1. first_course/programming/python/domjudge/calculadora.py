a, b, c = map(float, input().strip().split())

def calculadora(a, b, c):
    if c == 1:
        return a + b
    elif c == 2:
        return a - b
    elif c == 3:
        return a * b
    elif c == 4:
        return a / b

print("{:.1f}".format(calculadora(a, b, c)))