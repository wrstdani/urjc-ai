# Implementación del algoritmo "MergeSort" (divide y vencerás)
def merge(merged, izq, der):
    idx_izq = 0  # índice array izquierdo
    idx_der = 0  # índice array derecho
    idx_merged = 0  # índice array de fusión

    while idx_izq < len(izq) and idx_der < len(der):
        if izq[idx_izq] < der[idx_der]:   # si el primer entero del array izquierdo es menor que el primero del derecho:
            merged[idx_merged] = izq[idx_izq]   # metemos el primer elemento del array izquierdo en el array de fusión
            idx_izq += 1  # aumentamos en 1 el índice del array izquierdo
        else:   # si el primer elemento del array derecho es menor o igual que el primero del array izquierdo:
            merged[idx_merged] = der[idx_der]   # metemos el primer elemento del array derecho en el array de fusión
            idx_der += 1    # aumentamos en 1 el índice del array derecho
        idx_merged += 1  # en cada iteración aumentamos en 1 el índice del array de fusión
    # elementos "sobrantes"
    while idx_izq < len(izq):
        merged[idx_merged] = izq[idx_izq]
        idx_izq += 1
        idx_merged += 1

    while idx_der < len(der):
        merged[idx_merged] = der[idx_der]
        idx_der += 1
        idx_merged += 1


def merge_sort(array):
    if len(array) > 1:  # siempre que el array tenga más de 1 entero
        array_izq = array[:len(array)//2]  # el array izquierdo será la primera mitad del array original
        array_der = array[len(array)//2:]  # el array derecho será la segunda mitad del array original
        # implementamos la recursividad
        merge_sort(array_izq)
        merge_sort(array_der)
        # llamamos a la función de fusión
        merge(array, array_izq, array_der)


vector = [4, 2, 3, 1, 2, 7, 6]  # vector ejemplo
merge_sort(vector)  # llamada a función de ordenación
print(vector)
