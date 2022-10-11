n = int(input('Introduzca un valor mayor que 1: '))
pa = (n - 1)
pp = (n + 1)


def es_primo(n):
    while n > 1:
        if (n == 2):
            return True
        elif (n > 2):
            for i in range(2, n):
                if n % i == 0:
                    return False
                else:
                    return True

if es_primo(n) == True:
    print(str(n) + ' es primo.')

elif es_primo(n) == False:   
    def es_primo_ant(pa):
        if (pa == 2):
            return True

        elif (pa > 2):
            for i in range(2, pa):
                if (pa % i) == 0:
                    while (pa % i) == 0:
                        pa = pa - 1
                
                else:
                    return True
    
    def es_primo_post(pp):
        for i in range (2, pp):
            if (pp % i) == 0:
                while (pp % i) == 0:
                    pp = pp + 1

            else:
                return True
        


    if (es_primo_ant(pa) == True) and (es_primo_post(pp) == True):
        print(str(pa) + ' ' + str(pp))


elif (n <= 1):
    print('El valor ha de ser mayor que uno.')
    exec(open("P3Ej8.py").read())
