num = int(input('Introduzca el valor para calcular su factorial: '))

def factorial(num):
    if num == 1 or num == 0:
        resultado = 1
    
    elif num > 1:
        resultado = num * factorial(num - 1)    
    
    return resultado

fact_num = factorial(num)

print('El factorial de ' + str(num) + ' es ' + str(fact_num) + '.')