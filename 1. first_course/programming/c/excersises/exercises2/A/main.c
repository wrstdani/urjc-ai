#include <stdio.h>
#define eur_dol 1.19

int main() {
    double n;
    scanf("%lf", &n);
    double conv = (n * eur_dol);
    printf("%.2lf", conv);
    return 0;
}
