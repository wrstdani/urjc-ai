#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100

int main() {
    int random[N], count = 0, maxV = 0;

    srand(time(NULL));

    for (int i = 0; i < N; ++i) {
        *(random + count) = rand();
        count++;
    }

    count = 0;

    for (int j = 0; j < N; ++j) {
        if (maxV < *(random + count)) {
            maxV = *(random + count);
        }

        count++;
    }

    printf("Array: ");
    for (int a = 0; a < N; ++a) {
        printf("%i ", random[a]);
    }

    printf("\nMaximo: %i", maxV);

    return 0;
}
