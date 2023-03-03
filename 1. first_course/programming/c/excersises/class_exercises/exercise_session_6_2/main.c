#include <stdio.h>
#include <strings.h>
#define ROWS 4
#define COLS 3

void invierte(int *matriz);

int main() {
    int matriz1[ROWS][COLS], contador1 = 1;

    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            matriz1[i][j] = contador1;
            contador1++;
        }
    }

    invierte(matriz1);

    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            printf("%i\t", matriz1[i][j]);
        }
        printf("\n");
    }


    return 0;
}

void invierte(int *matriz) {
    int contador2 = ROWS * COLS;
    for (int i = 0; i < ROWS * COLS; ++i) {
        *(matriz + i) = contador2;
        contador2--;
    }
}