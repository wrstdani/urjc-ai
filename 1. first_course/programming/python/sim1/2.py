def ond_tres_cifras(num):
    if (((num % 10) * 100) + ()) == num:
        return "Es ondulado"
    else:
        return "No es ondulado"


num = int(input())
print(ond_tres_cifras(num))