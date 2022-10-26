caracter = input()
count_coma = 0

while not caracter.__contains__('*'):
    if caracter.__contains__(','):
        count_coma += 1
    
    caracter = input()

print(str(count_coma))