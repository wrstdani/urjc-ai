vm = int(input('Inserte el candidato a valor máximo:'))
a = int(input('Inserte el valor del primer término a comparar:'))
b = int(input('Inserte el valor del segundo término a comparar:'))
c = int(input('Inserte el valor del tercer término a comparar:'))
d = int(input('Inserte el valor del cuarto término a comparar:'))

lista = [a, b, c, d]

for i in lista:
    if vm >= i:
        print(str(vm) + ', tu candidato a valor máximo, es el valor máximo frente a ' + str(i) + '.')

    elif vm < i:
        print(str(i) + ' es el valor máximo frente a ' + str(vm) + ', tu candidato a valor máximo.')