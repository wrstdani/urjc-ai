//
// Created by ddeln on 2/18/2023.
//

#include <stdio.h>

int triangle(int x) {
    int limite = 0;

    for (int i = 1; i <= x; i++) {
        while (limite != i) {
            printf("*");
            limite++;
        }
        limite = 0;
        printf("\n");
    }

    return 0;
}

int square(int x) {
    for (int i = 0; i < x; ++i) {
        for (int j = 0; j < x; j++) {
            if (i == 0 || i == (x-1)) {
                printf("*");
            } else {
                if (j == 0 || j == (x-1)) {
                    printf("*");
                } else {
                    printf(" ");
                }
            }
        }
        printf("\n");
    }

    return 0;
}

int pyramid(int x) {
    int nEspacios;

    for (int fila = 1; fila <= x; fila++) {
        for (int columna = 1; columna <= x; columna++) {

        }
    }

    return 0;
}

int diamond(int x) {


    return 0;
}


int menu() {
    int a, b;

    printf("Give me two integers, the first will decide the shape and the second the base of it.\n");
    printf("(1) Triangle\n(2) Square\n(3) Pyramid\n(4) Diamond\n");

    scanf("%i", &a);

    while (a != 0) {
        scanf("%i", &b);

        if (a == 1) {
            triangle(b);
        } else if (a == 2) {
            square(b);
        } else if (a == 3) {
            pyramid(b);
        } else if (a == 4) {
            diamond(b);
        } else {
            printf("You just gave me an invalid integer (range 1 to 4)\n");
        }

        menu();
    }

    printf("Exiting program...\n");

    return 0;
}

