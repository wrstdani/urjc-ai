#include <stdio.h>

// Hello world
int hello_world() {
    printf("Hello, world!\n");
    return 0;
}

// Average value
int average() {
    float a, b, c, result;
    printf("\nCalculate the average of three numbers\n");
    printf("\nIntroduce number a: ");
    scanf("%f", &a);
    printf("\nIntroduce number b: ");
    scanf("%f", &b);
    printf("\nIntroduce number c: ");
    scanf("%f", &c);
    result = ((a+b+c)/3);
    printf("The average value of %f, %f and %f is: %f", a, b, c, result);
    return 0;
}

int range_to_value() {
    int value;
    printf("\nIntroduce a value: ");
    scanf("%i", &value);
    for (int i=1; i<=value; i++) {
        printf("\n%i\n", i);
    }
    return 0;
}

int main() {
    hello_world();
    average();
    range_to_value();
    return 0;
}