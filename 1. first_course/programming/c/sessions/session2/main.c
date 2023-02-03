//
// Created by ddeln on 03/02/2023.
//
#include <stdio.h>
int main() {
    int x = 2;
    short int y  = 4;
    unsigned short int z = 8;
    unsigned int w = 10;
    float a = 2.5;
    double b = 5.6;
    long double c = 8.7;
    char u = 'j';

    printf("INT: %i\n", sizeof(x));
    printf("SHORT INT: %i\n", sizeof(y));
    printf("UNSIGNED SHORT INT: %i\n", sizeof(z));
    printf("UNSIGNED INT: %i\n", sizeof(w));
    printf("FLOAT: %i\n", sizeof(a));
    printf("DOUBLE: %i\n", sizeof(b));
    printf("LONG DOUBLE: %i\n", sizeof(c));
    printf("CHAR: %i\n", sizeof(u));

    return 0;
}