def descomponer(n):
    divisor = 2
    lista = []
    while n > 1:
        if n % divisor == 0:
            lista.append(divisor)
            n = n // divisor
            
        else:
            divisor += 1
    return lista


print('Programa que calcula la descomposición en factores primos de un número \n')
numero = int(input('Dame el número: '))
factores = descomponer(numero)
print('La lista de factores primos de', numero, 'es: ', factores)