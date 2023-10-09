#include <stdio.h>
#include <time.h>

int main() {
    int n = 1000000000;
    int a = 0;

    time_t t0 = clock();

    for (int i = 0; i < n; ++i) {
        a++;
    }

    time_t t1 = clock();

    double tiempo = (double)(t1 - t0)/CLOCKS_PER_SEC;

    printf("Ha tardado %f segundos.\n", tiempo);

    return 0;
}
