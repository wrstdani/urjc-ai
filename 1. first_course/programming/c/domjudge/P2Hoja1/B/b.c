#include <stdio.h>

int main() {
    int n, m;
    scanf("%i", &n);
    scanf("%i", &m);
    float resultado = (n*m*1000000);
    float resultado_a = (resultado/1000);
    int resultado_b = (resultado_a/2);
    printf("%i", resultado_b);
    return 0;
}