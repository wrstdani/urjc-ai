def sumaCifrasRec(numero):
    if numero < 10:
        result = numero
    else:
        unidad = numero % 10
        result = unidad + sumaCifrasRec(numero // 10)
    return result

x = int(input())

print(sumaCifrasRec(x))
