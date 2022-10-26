n = int(input())
def cifras(n):
    if n < 10:
        return 1
    else:
        return 1 + cifras(n // 10)

def voltear_numero(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10 ** (cifras(n) - 1) + voltear_numero(n // 10)

print(cifras(n), voltear_numero(n))