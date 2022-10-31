n = int(input())
n1 = n
cifras = 0
a = n % 10
n = n // 10
b = n % 10
n = n // 10

while n1 > 0:
    cifras += 1
    n1 = n1 // (10)

caso = True
ondulado = True

if cifras >= 3:
    while n > 0:
        res = n % 10
        if caso:
            if res != a:
                ondulado = False
        else:
            if res != b:
                ondulado = False
        caso = not caso
        n = n // 10
    print(ondulado)

else:
    print('El número ha de contar con 3 o más cifras.')

