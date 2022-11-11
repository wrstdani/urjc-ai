def cifras(x, y):
    while x // (10 ** y) > 0:
        return cifras(x, y + 1)
    return y

num_cifras = 1
print(cifras(0, num_cifras))