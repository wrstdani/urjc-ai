def rot(words_in_abc, abc):
    d = int(input(''))  # Introducir desplazamiento
    frase = str(input(''))  # Introducir frase
    for s in frase:
        if s != ' ':
            if frase.index(s) + d < words_in_abc:
                frase.replace(frase[frase.index(i)])

n = int(input(''))
words_in_abc = 26
abc = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    print(rot(words_in_abc, abc))
