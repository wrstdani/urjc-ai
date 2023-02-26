#include <stdio.h>
#define N 10

int main() {
    int a, b, count = 1, add[N], sub[N];

    printf("Give me two integers to calculate the series: ");
    scanf("%i %i", &a, &b);

    for (int i = 0; i < N; ++i) {
        add[i] = count * (a + b);
        sub[i] = count * (a - b);
        count++;
    }

    printf("Suma: ");
    for (int j = 0; j < N; ++j) {
        printf("%i ", add[j]);
    }

    printf("\n");

    printf("Resta: ");
    for (int c = 0; c < N; ++c) {
        printf("%i ", sub[c]);
    }

    return 0;
}
