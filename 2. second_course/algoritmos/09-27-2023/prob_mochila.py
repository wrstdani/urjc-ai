# Función para imprimir los objetos de la mochila con sus respectivos pesos y valores
def imprimirMochila(dicObjetos):
    for objeto, datos in dicObjetos.items():
        print(objeto, ":", datos["peso"], ",", datos["valor"])


# Función para insertar los objetos de la mochila con sus respectivos pesos y valores
def inicializarMochila(n, dicObjetos):
    for i in range(n):
        nombre = input("Introduce el nombre del objeto %d: " % (i+1))
        peso = int(input("Introduce el peso del objeto %d: " % (i+1)))
        valor = int(input("Introduce el valor del objeto %d: " % (i+1)))
        dicObjetos[nombre] = {
            "peso" : peso,
            "valor" : valor,
            "peso-valor" : (peso / valor)
        }
    return dicObjetos


# Función para seleccionar el objeto con mejor relación peso-valor y comprobar si el objeto cabe en la mochila
def cabeObjetoMax(pesoSoportado, dicObjetos):
    listaPesoValor = []
    listaPeso = []
    for objeto, datos in dicObjetos.items():
        listaPeso.append(datos["peso"])
        listaPesoValor.append(datos["peso-valor"])
    return pesoSoportado >= listaPeso[listaPesoValor.index(max(listaPesoValor))]


def fraccion(cabeObjetoMax):
    


# PROGRAMA PRINCIPAL
n = int(input("Introduce el número de objetos: ")) # Número de objetos a meter en la mochila
dicObjetos = {}
pesoSoportado = int(input("Introduce el peso que soporta la mochila: "))

print(cabeObjetoMax(pesoSoportado, inicializarMochila(n, dicObjetos)))