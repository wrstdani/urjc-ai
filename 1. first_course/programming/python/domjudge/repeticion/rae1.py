n = int(input())
lista = []
frase_correcta = ''

for i in range(n):
    frase = input()
    lista.append(frase)

for j in lista:
    if '.' not in frase:
        print('Perfecto')
    
    else:
        frase_lista = list(frase)
        letra = frase_lista[(frase_lista.index('.')) + 1]
        
        if letra == letra.upper():
            print('Perfecto')
        
        else:
            frase_lista[frase_lista.index(letra)] = letra.upper()
            for a in range(len(frase_lista)):
                frase_correcta = frase_correcta + frase_lista[a]
            
            print('ZOQUETE se dice:', frase_correcta)
