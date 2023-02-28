#include <stdio.h>
#define FILAS 4
#define COLS 3

int main() {
    int matriz[FILAS][COLS], contador = 1;

    for (int i = 0; i < FILAS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            matriz[i][j] = contador;
            contador++;
        }
    }

    printf("La matriz es: \n");

    for (int a = 0; a < FILAS; ++a) {
        for (int b = 0; b < COLS; ++b) {
            printf("%i\t", matriz[a][b]);
        }
        printf("\n");
    }

    return 0;
}
