#include <stdio.h>

int main() {
    int m, v;
    scanf("%i %i", &m, &v);
    int nveces = m * v;

    for (int i = 0; i < nveces; i++) {
        printf("Sin tele y sin cerveza, Homer pierde la cabeza\n");
    }

    return 0;
}