def pedirValores():
    real = float(input('Parte real del número: '))
    imaginaria = float(input('Parte imaginaria del número: '))
    numComplejo = {}
    numComplejo['real'] = real
    numComplejo['imaginaria'] = imaginaria
    return numComplejo

def imprimir(c):
    print(c['real'], '+', c['imaginaria'], 'i')

def sumar(c1, c2):
    suma = {}
    suma['real'] = c1['real'] + c2['real']
    suma['imaginaria'] = c1['imaginaria'] + c2['imaginaria']
    return 'El resultado de la suma es %s + %s i' % (suma['real'], suma['imaginaria'])


c1 = pedirValores()
c2 = pedirValores()
imprimir(c1)
imprimir(c2)
print(sumar(c1, c2))