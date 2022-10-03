euros = float(input('Introduzca la cantidad deseada de capital en euros:'))
interes = float(input('Introduzca la tasa de interés deseada en porcentaje:'))
años = float(input('Introduzca el número de años:'))

capital_final = int(euros * (años ** (1 + interes/100)))

print('El capital total tras el tiempo introducido será de', capital_final, '€.')
