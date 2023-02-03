def esCongruente(x, y, z):
    if y < 0:
        y += z
    n = x - y
    
    if n % z == 0:
        return 'Es verdad que %s ≡ %s (mod %s)' % (x, y, z)

    else:
        return 'Es falso que %s ≡ %s (mod %s)' % (x, y, z)


a = int(input('Introduce a: '))
b = int(input('Introduce b: '))
m = int(input('Introduce m: '))

print(esCongruente(a, b, m))