#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Función búsqueda secuencial (O(n)): itera a lo largo del array hasta
// encontrar el elemento.
double busquedaSecuencia(int *array, int tam, int elem);

// Función búsqueda binaria (O(log n)): divide el array ORDENADO y evalua
// si el elemento se ha encontrado en una mitad y si no busca en la otra
// mitad.
int busquedaBinaria(int *array, int tam, int elem);

// Función ordenación directa (O(n^2)): ordena el array con dos bucles
// y ordenando por comparacion.
int *ordenacionDirecta(int *array, int tam);

// Función ordenación por mezcla (O(n log n)): ordena el array comparando
// cada elemento con su "vecino" (i+1), y seguidamente comparando parejas,
// cuartetos, etc.
int *ordenacionPorMezcla(int *array, int tam);


int main() {
    int tam = 2147483647;
    int array[tam];


    return 0;
}

double busquedaSecuencia(int *array, int tam, int elem) {
    // Declaramos e inicializamos t0.
    time_t t0 = clock();
    time_t t1 = 0;
    // Bucle que recorre el array.
    for (int i = 0; i < tam; ++i) {
        // Si el elemento del array coincide con el elemento que buscamos
        // se para el bucle.
        if (array[i] == elem) {
            t1 = clock();
            break;
        }
    }
    double tiempoFinal = (double)(t1-t0)/CLOCKS_PER_SEC;
    return tiempoFinal;
}