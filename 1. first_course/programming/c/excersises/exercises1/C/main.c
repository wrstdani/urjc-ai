#include <stdio.h>

int main() {
    double base, height;
    printf("Give me the base of the triangle:\n");
    scanf("%lf", &base);
    printf("Give me the height of the triangle:\n");
    scanf("%lf", &height);
    double result = (base * height) / 2;
    printf("The area of the triangle is of %.2lf", result);
    return 0;
}