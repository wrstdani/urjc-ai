#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

int main() {
    int serie1[N], serie2[N], serieSuma[N];

    srand(time(NULL));

    for (int i = 0; i < N; ++i) {
        serie1[i] = rand();
        serie2[i] = rand();
        serieSuma[i] = serie1[i] + serie2[i];
    }

    printf("Serie 1: ");
    for (int j = 0; j < N; ++j) {
        printf("%i ", serie1[j]);
    }

    printf("\nSerie 2: ");
    for (int a = 0; a < N; ++a) {
        printf("%i ", serie2[a]);
    }

    printf("\nSuma: ");
    for (int b = 0; b < N; ++b) {
        printf("%i ", serieSuma[b]);
    }

    return 0;
}
