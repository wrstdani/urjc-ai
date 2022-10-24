print('\nEste programa muestra todos los números primos entre 2 y 100.\n')

print('Los números primos entre 2 y 100 son: ')

num = 2

while num <= 100:
    esPrimo = True
    divisor = 2

    while divisor < num and esPrimo:
        esPrimo = num % divisor != 0
        divisor += 1
    
    if esPrimo:
        print(num, end = ' ')
    num += 1

print('\n')