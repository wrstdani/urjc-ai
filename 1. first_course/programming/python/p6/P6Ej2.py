def sust_neg(x):
    for i in x:
        if i < 0:
            x[x.index(i)] = 0
    return x


a = [-1, 3, 4, 7, -23, -9]

print('Este programa convierte los valores negativos de una lista a cero \n')
print(a)
print(sust_neg(a))