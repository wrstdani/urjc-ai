#include <stdio.h>
#include <math.h>

int main() {
    int n;
    scanf("%i", &n);
    if (n < 0) {
        printf("Error: n must be positive");
    } else {
        printf("The square root of %i is %.2f", n, sqrt(n));
    }
    return 0;
}