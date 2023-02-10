#include <stdio.h>
int example1() {
    int a = 7;
    int b;
    int *p;

    p = &a;
    b = *p;

    printf("Valor de b es %i", b);
    return 0;
}

int example2() {
    int a = 1;
    int *pa, *pb, *pc;

    pa = &a;
    pb = &a;
    pc = &a;

    *pa = *pa + 1;
    *pb = *pb + 1;
    *pc = *pc + 1;

    return 0;
}

int example3() {
    int a = 5;
    int *b;

    b = &a;

    printf("El valor de a es %i", a);
    printf("La direccion de a es %p", &a);

    printf("El valor de b es %p", b);
    printf("La indireccion de b es %i", *b);
    printf("La direccion de b es %p", &b);

    return 0;
}

int main() {

}
