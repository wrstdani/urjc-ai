#include <stdio.h>

int main() {
    int n, m;
    printf("Give me two numbers (ints): ");
    scanf("%i %i", &n, &m);
    if (m == 0) {
        printf("Can't divide by zero.");
    } else {
        int resultado = n / m;
        printf("The result is %i.", resultado);
    }

    return 0;
}