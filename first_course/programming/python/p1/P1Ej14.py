salario_base = 1500
ventas = float(input('Introduzca el valor de las ventas del mes:'))

salario_bruto = 1500 + ((3 * ventas)/100)
salario_neto = salario_bruto - ((18 * salario_bruto)/100)

print('El salario bruto es de:', salario_bruto, '€.')
print('El salario neto es de:', salario_neto, '€.')