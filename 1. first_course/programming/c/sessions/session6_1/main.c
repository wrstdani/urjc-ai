#include <stdio.h>
#define N 10

void resetea(int *valor) {
    *valor = 0;
}

void reseteaArray(int *vector) {
    for (int i = 0; i < N; ++i) {
        vector[i] = 0;
    }
}

int main() {
    int a = 7, vector[N];
    for (int i = 0; i < N; ++i) {
        vector[i] = i;
    }

    printf("Los valores iniciales del array son: \n");

    for (int j = 0; j < N; ++j) {
        if (j == (N - 1)) {
            printf("%i", vector[j]);
        } else {
            printf("%i, ", vector[j]);
        }
    }

    printf("\nEl valor inicial de la variable es %i.\n", a);

    resetea(&a);
    reseteaArray(vector);

    printf("Los valores finales del array son: \n");

    for (int c = 0; c < N; ++c) {
        if (c == (N - 1)) {
            printf("%i", vector[c]);
        } else {
            printf("%i, ", vector[c]);
        }
    }

    printf("\nEl valor final de la variable es %i.\n", a);

    return 0;
}
