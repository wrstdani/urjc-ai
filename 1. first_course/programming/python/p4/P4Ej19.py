def suma_naturales(a):
    resultado = 0
    if a >= 1:
        resultado = a + (suma_naturales(a - 1))        
    return resultado

n = int(input('Introduzca el límite de la suma en los números naturales: '))

while n < 0:
    n = int(input('El número ha de ser mayor que cero: '))

print('El resultado de la suma de los n primeros números naturales es:', suma_naturales(n))