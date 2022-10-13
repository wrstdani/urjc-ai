n = int(input('Introduzca un valor entero: '))
na = (n - 1)
np = (n + 1)

if (n <= 1):
    print('Ha introducido un valor igual o menor a uno, por lo que el programa se cerrará.')
    quit

elif (n > 1):
    def es_primo(n):
        if (n == 2):
            return True

        elif (n > 2):
            for i in range (2, n):
                if (n % i) == 0:
                    return False
                
                else:
                    return True

    def es_primo_ant(na):
        if na == 2:
            return True

        for i in range (2, na):
            while na % i == 0:
                return False

    def es_primo_post(np):
        for i in range (2, np):
            while np % i == 0:
                return False

    
while es_primo_ant(na) == False:
    na = na - 1

while es_primo_post(np) == False:
    np = np + 1

if (es_primo(n) == True):
    print('El número primo inmediatamente anterior a ' + str(n) + ' es ' + str(na) + ' y el inmediatamente posterior es ' + str(np) + '. ')
    print('Además, el número introducido (' + str(n) + ') es primo.')
    
else:
    print('El número primo inmediatamente anterior a ' + str(n) + ' es ' + str(na) + ' y el inmediatamente posterior es ' + str(np) + '. ')