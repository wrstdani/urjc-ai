#include <stdio.h>

int main() {
    double a, b, result;
    int c;
    
    scanf("%lf %lf %i", &a, &b, &c);

    if (c == 1) {
        result = a + b;
    } else if (c == 2){
        result = a - b;
    } else if (c == 3){
        result = a * b;
    } else if (c == 4) {
        result = a / b;
    }

    printf("%.1lf", result);

    return 0;
}