def rot(x, l):
    frase_lista = list(l)
    for char in frase_lista:
        if char != ' ':
            if char in abc:
                letra_pos = abc.index(char)
                pos_final = letra_pos + x
                while pos_final > 25:
                    pos_final -= 26
                letra_final = abc[pos_final]
                frase_lista[frase_lista.index(char)] = letra_final

            elif char in abc_may:
                letra_pos = abc_may.index(char)
                pos_final = letra_pos + x
                while pos_final > 25:
                    pos_final -= 26
                letra_final = abc[pos_final]
                frase_lista[frase_lista.index(char)] = letra_final

    return frase_lista

lista = []
abc = 'abcdefghijklmnopqrstuvwxyz'
abc_may = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())

for i in range(n):
    d = int(input())
    s = input()
    lista.append(rot(d, s))

print(lista)
for t in lista:
    print(*t, sep='')