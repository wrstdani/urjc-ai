seg_inp = int(input())

if (seg_inp >= 3600):
    horas = (seg_inp // 3600)
    minutos =0
    segundos = 0

    if (seg_inp % 3600) > 0:
        minutos = ((seg_inp % 3600) // 60)

        if ((seg_inp % 60) != 0):
            segundos = (seg_inp % 60)

        else:
            segundos = 0

elif (60 <= seg_inp < 3600):
    horas = 0
    minutos = (seg_inp // 60)

    if ((seg_inp % 60) != 0):
        segundos = (seg_inp % 60)
    
    else:
        segundos = 0

print(horas, minutos, segundos)