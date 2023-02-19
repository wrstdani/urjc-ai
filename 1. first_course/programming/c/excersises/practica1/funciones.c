#include <stdio.h>
#include "funciones.h"

int menu() {
    int a, b;

    printf("Las opciones son las siguientes:\n(1) Triángulo\n(2) Cuadrado\n(3) Pirámide\n(4) Diamante\n");
    printf("Introduzca el número de la figura y el entero en la misma línea. El programa se cerrará cuando introduzca el número 0: ");

    scanf("%i %i", &b, &a);

    do {
        if (b < 0 || b > 4) {
            printf("El número introducido está fuera del rango (el rango es de 1 a 4, o 0 para cerrarlo).\n\n");
        } else if (b == 1) {
            triangle (a);
        } else if (b == 2) {
            square(a);
        } else if (b == 3) {
            pyramid(a);
        } else if (b == 4) {
            diamond(a);
        }
        menu();
    } while (b != 0);

    printf("Ha introducido 0, por lo que se cerrará el programa.\n");

    return 0;
}

int triangle(int x) {
    int limite = 0;

    for (int i = 0; i <= x; i++) {
        
        printf("\n");
        limite = 0;
    }

    return 0;
}

int square(int x) {

}

int pyramid(int x) {

}

int diamond(int x) {

}