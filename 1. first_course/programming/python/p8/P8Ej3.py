def añadir(x):
    nombre = input('Introduzca el nombre del contacto: ')
    phone = input('Introduzca el número de teléfono: ')
    x[nombre] = phone
    return 'Se ha añadido a %s con número %s' % (nombre, phone)

def eliminar(x):
    nombre = input('Introduzca el contacto que desea eliminar: ')
    for key in x.items():
        if nombre == key:
            del x[key]
    return 'Se ha eliminado el contacto %s.' % (nombre)

def consultar(x):
    nombre = input('Introduzca el nombre del contacto que desea consultar: ')
    for key, value in x.items():
        if nombre == key:
                return 'El contacto %s tiene el número %s.' % (nombre, value)

def imprimir(x):
    for key, value in x.items():
        print('Nombre: %s - Número: %s' % (key, value)) 


agenda = {}
a = True
while a == True:
    operacion = input('Añadir (a), Eliminar (b), Consultar (c), Imprimir (d): ')
    if operacion == 'a':
        print(añadir(agenda))
    if operacion == 'b':
        print(eliminar(agenda))
    if operacion == 'c':
        print(consultar(agenda))
    if operacion == 'd':
        imprimir(agenda)
    if operacion != 'a' and operacion != 'b' and operacion != 'c' and operacion != 'd':
        a = False
