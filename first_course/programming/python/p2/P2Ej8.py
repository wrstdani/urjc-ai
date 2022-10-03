euros = int(input('Introduzca una cantidad exacta de euros:'))

list = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for i in list:
    if euros >= i:
        dinero_restante = euros // i
        print('Hay ' + str(dinero_restante) + (' billete/s' if euros >= 5 else ' moneda/s') + ' de ' + str(i) + ' euros')
        euros = euros % i




