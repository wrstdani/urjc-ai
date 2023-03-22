#include <stdio.h>
#include <string.h>
#define MAX 20

enum Battle {
    DERROTA = 0,
    EMPATE = 1,
    VICTORIA = 3
};

struct persona {
    char nombre[MAX];
    char apes[MAX];
    short int edad;
};

void muestraPersona(struct persona per) {
    printf("La persona se llama %s %s y tiene %i.\n", per.nombre, per.apes, per.edad);
}
void ejercicio1(enum Battle varResultado);
void estados();

int main() {
    enum Battle varResultado;
    // Creamos el struct "persona" en el que se podran declarar nombres, apellidos y edades

    // Declaramos a la persona 1
    struct persona per1;
    // Asignamos el nombre a la persona 1
    strcpy(per1.nombre, "Dani");
    // Asignamos el appellido a la persona 1
    strcpy(per1.apes, "del Nuevo");
    // Asignamos la edad de la persona 1
    per1.edad = 18;
    //
    struct persona per2;
    // Copia todos los valores de per1 a per2
    per2 = per1;

    muestraPersona(per2);

    estados();

    ejercicio1(varResultado);

    return 0;
}

void ejercicio1(enum Battle varResultado) {
    switch(varResultado) {
        case DERROTA:
            printf("Derrota!\n");
            break;
        case EMPATE:
            printf("Empate!\n");
            break;
        case VICTORIA:
            printf("Victoria!\n");
            break;
        default:
            printf("Resultado incorrecto!");
    }
    printf("Hemos sumado %i puntos", varResultado);
}

void estados() {
    enum tEstados {
        SOLIDO,
        LIQUIDO,
        GASEOSO
    };

    enum tEstados estado = 0;

    printf("Estado es %i\n", estado);

    estado++;

    if(estado == LIQUIDO) printf("Estado liquido!!!\n");
}