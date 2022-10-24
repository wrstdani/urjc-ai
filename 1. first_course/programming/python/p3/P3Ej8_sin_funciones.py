print('\n Este programa imprime el número primo inmediatamente posterior y anterior a el introducido por el usuario. \n')

numInput = int(input('Introduzca un valor: '))
primoAnt = numInput - 1
primoPost = numInput + 1

if primoAnt == 2:
    esPrimoAnt = True

elif primoAnt > 2:
    esPrimoAnt = False

    for i in range (2, numInput + 1):
        while esPrimoAnt == False:
            primoAnt -= 1

            if primoAnt % i != 0:
                esPrimoAnt = True
            
            else: 
                esPrimoAnt = False


if esPrimoAnt == True:
    print(str(primoAnt))

if 
        