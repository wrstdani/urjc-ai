#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    printf("El numero de argumentos es %i", argc);

    int tercero;

    if (argc == 3) {
        tercero = atoi(argv[2]);
        printf("\nEl numero es %i", tercero);
    } else {
        printf("\nNumero de arguento incorrecto. \nLLamada: programa <cadena> <entero>");
    }

    return 0;
}
