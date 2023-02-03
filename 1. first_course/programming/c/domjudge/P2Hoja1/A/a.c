#include <stdio.h>

int main() {
    int n, m;
    scanf("%i", &n);
    scanf("%i", &m);
    float resultado = (n*m);
    float resultado_conv = resultado/1000;
    printf("%.1f", resultado_conv);
    return 0;
}