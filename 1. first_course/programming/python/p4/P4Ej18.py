def factorial(a):
    if a == 0 or a == 1:
        resultado = 1
    elif a > 1:
        resultado = a * (factorial(a - 1))        
    return resultado


def combinaciones(x, y):
    output = factorial(x) / (factorial(y) * factorial(x - y))
    return output

n = int(input('Introduzca un valor: '))
m = int(input('Introduzca un valor entre 0 y el anterior: '))

print('El número combinatorio es', combinaciones(n, m))