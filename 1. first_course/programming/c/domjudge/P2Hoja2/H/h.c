/*
    Factorial in C
    @wrstdani
*/

#include <stdio.h>

int main() {
    double n, factorial = 1.0;
    scanf("%lf", &n);

    for (int i = n; i > 1; i--) {
        factorial *= i;
    }
    printf("%.0lf", factorial);

    return 0;
}