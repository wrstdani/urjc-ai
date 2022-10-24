n = int(input())
m = int(input())

litros_totales = (n * (m * (10 ** 6))) // 1000

botellas = litros_totales // 2

print(botellas)