#include <stdio.h>
#include <stdlib.h>

int ejercicioSumaResta(int *x, int *y);

int main() {
    int a, b;

    printf("Dame dos enteros: ");
    scanf("%i %i", &a, &b);

    int random = ejercicioSumaResta(&a, &b);
    printf("Se ha operado los valores anteriores con %i dando %i y %i.", random, a, b);

    return 0;
}

int ejercicioSumaResta(int *x, int *y) {
    int rnd = rand();
    *x += rnd;
    *y -= rnd;
    return rnd;
}