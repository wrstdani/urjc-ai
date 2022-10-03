day = int(input('Introduzca un día (numéricamente): '))
month = int(input('Introduzca un mes (numéricamente): '))
year = int(input('Introduzca un año (numéricamente): '))

if year > 0:
    if month == 1:
        if 1 <= day <= 31:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de enero son del 1 al 31.')


    if month == 2:
        # Año bisiesto
        if year % 4 == 0 or year % 400 == 0:
            if 1 <= day <= 29:
                print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

            else:
                print('La fecha es errónea, puesto que en febrero, en un año bisiesto como ' + str(year) + ', los días son del 1 al 29.')


        else:
            if 1 <= day <= 28:
                print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

            else: 
                print('La fecha es errónea, puesto que en febrero, en un año no bisiesto como ' + year + ', los días son del 1 al 28.')


    if month == 3:
        if 1 <= day <= 31:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de marzo son del 1 al 31.')


    if month == 4:
        if 1 <= day <= 30:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de abril son del 1 al 30.')


    if month == 5:
        if 1 <= day <= 31:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de mayo son del 1 al 31.') 

        
    if month == 6:
        if 1 <= day <= 30:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de junio son del 1 al 30.')


    if month == 7:
        if 1 <= day <= 31:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de julio son del 1 al 31.')
    

    if month == 8:
        if 1 <= day <= 31:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de agosto son del 1 al 31.')

    
    if month == 9:
        if 1 <= day <= 30:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de septiembre son del 1 al 30.')


    if month == 10:
        if 1 <= day <= 31:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de octubre son del 1 al 31.')


    if month == 11:
        if 1 <= day <= 30:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de noviembre son del 1 al 30.')


    if month == 12:
        if 1 <= day <= 31:
            print('La fecha es correcta, siendo esta: ' + str(day) + '/' + str(month) + '/' + str(year))

        else:
            print('La fecha es errónea, puesto que los días de diciembre son del 1 al 31.')


    else:
        print('La fecha es errónea puesto que los meses van del 1 al 12.')



else:
    print('La fecha es errónea puesto que los años se cuentan a partir del 0 (no inclusive).')