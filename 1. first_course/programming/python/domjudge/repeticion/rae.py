n = int(input())

abc_min = 'abcdefghijklmnopqrstuvwxyz'
abc_may = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lista = []
for i in range(n):
    frase = input()

    frase_a_p = frase.split('.')[0]
    frase_d_p = frase.split('.')[1]

    if '.' not in frase:
        lista.append('Perfecto')

    else:
        if frase_d_p.strip()[0] in abc_min:
            lista.append('ZOQUETE se dice: ' + frase_a_p + '.' + (frase_d_p.strip()).replace(frase_d_p.strip()[0], abc_may[abc_min.index((frase_d_p.strip())[0])]))
        else:
            lista.append('Perfecto')

for x in lista:
    print(x)