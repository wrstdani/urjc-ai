def CrearConjuntoVacio():
    return []


def añadirElemento():
    conjunto1 = []
    nElementos1 = int(input('Introduzca el número de elementos que tendrá su conjunto: \n'))

    for i in range(nElementos1):
        elemento1 = input('Introduzca el elemento del conjunto: \n')
        conjunto1.append(elemento1)
    
    elementoAñadir = input('Introduzca el elemento que desea añadir al conjunto indtroducido: \n')
    
    while elementoAñadir in conjunto1:
        elementoAñadir = input('El elemento que desea añadir ya se encuentra en el conjunto. Por favor, inténtelo de nuevo: \n')
    conjunto1.append(elementoAñadir)

    return conjunto1


def borrarElemento():
    conjunto2 = []
    elementoBorrar = input('Introduzca el elemento que desea eliminar del conjunto: \n')
    nElementos2 = int(input('Introduzca el número de elementos de su conjunto: \n'))

    for j in range(nElementos2):
        elemento2 = input('Introduzca el elemento del conjunto: \n')
        conjunto2.append(elemento2)

    while elementoBorrar not in conjunto2:
        elementoBorrar = input('El elemento introducido no está en el conjunto. Inténtelo de nuevo: \n')
    
    conjunto2.remove(elementoBorrar)

    return conjunto2


def union():
    conjuntoUnion = []
    conjunto11 = []
    conjunto12 = []

    nElementos11 = int(input('Introduzca el número de elementos del primer conjunto: \n'))
    for i in range(nElementos11):
        elemento11 = input('Introduzca el elemento para añadir al primer conjunto: \n')
        conjunto11.append(elemento11)
    
    nElementos12 = int(input('Introduzca el número de elementos del segundo conjunto: \n'))
    for j in range(nElementos12):
        elemento12 = input('Introduzca el elemento para añadir al segundo conjunto: \n')
        conjunto12.append(elemento12)

    conjuntoUnion.append(conjunto11)
    conjuntoUnion.append(conjunto12)

    return conjuntoUnion


def interseccion():
    conjuntoInter = []
    conjunto21 = []
    conjunto22 = []

    nElementos21 = int(input('Introduzca el número de elementos del primer conjunto: \n'))
    for i in range(nElementos21):
        elemento21 = input('Introduzca el elemento para añadir al primer conjunto: \n')
        conjunto21.append(elemento21)

    nElementos22 = int(input('Introduzca el número de elementos del segundo conjunto: \n'))
    for j in range(nElementos22):
        elemento22 = input('Introduzca el elemento para añadir al segundo conjunto: \n')
        conjunto22.append(elemento22)

    for x in conjunto21:
        if x in conjunto22:
            conjuntoInter.append(x)

    return conjuntoInter


def diferencia():
    conjuntoDif = []
    conjunto31 = []
    conjunto32 = []

    nElementos31 = int(input('Introduzca el número de elementos del primer conjunto: \n'))
    for i in range(nElementos31):
        elemento31 = input('Introduzca el elemento para añadir al primer conjunto: \n')
        conjunto31.append(elemento31)

    nElementos32 = int(input('Introduzca el número de elementos del segundo conjunto: \n'))
    for j in range(nElementos32):
        elemento32 = input('Introduzca el elemento para añadir al segundo conjunto: \n')
        conjunto32.append(elemento32)

    for x  in conjunto31:
        if x not in conjunto32:
            conjuntoDif.append(x)

    return conjuntoDif
    

print(CrearConjuntoVacio())
print(añadirElemento())
print(borrarElemento())
print(union())
print(interseccion())
print(diferencia())