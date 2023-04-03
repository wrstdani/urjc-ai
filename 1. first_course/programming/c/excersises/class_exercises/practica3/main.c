#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX1 20
#define MAX2 100

typedef struct {
    char nombre[MAX1];
    char apellidos[MAX2];
    char telefono[MAX1];
    short int edad;
    char tipo[MAX1];
} tAgenda;

void printContactos(int nContactos, tAgenda *agenda);

int main() {
    int nContactos = 0, opcion;
    tAgenda *agenda;

    agenda = malloc(sizeof(tAgenda));

    printf("Bienvenido a tu agenda programada en C!\n");
    printf("---------------------------------------\n");
    
    do {
        printf("1 - Listado de personas\n");
        printf("2 - Nueva persona\n");
        printf("3 - Borrar persona\n");
        printf("4 - Guardar agenda en fichero de texto\n");
        printf("5 - Leer agenda de fichero de texto\n");
        printf("0 - Salir\n");
        printf("---------------------------------------\n");

        printf("Elije una de las opciones: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1:
                printContactos(nContactos, agenda);
                break;

            case 2:
                nContactos++;
                realloc(agenda, sizeof(tAgenda) * nContactos);
                printf("DATOS CONTACTO %d:\n", (nContactos));
                printf("Nombre: ");
                gets(agenda[nContactos-1].nombre);
                printf("Apellidos: ");
                gets(agenda[nContactos-1].apellidos);
                printf("Telefono: ");
                scanf("%s", agenda[nContactos-1].telefono);
                printf("Edad: ");
                scanf("%hu", &agenda[nContactos-1].edad);
                printf("Tipo de contacto: (1) FAVORITO, (2) CONOCIDO, (3) TRABAJO: ");
                int tipo;
                scanf("%d", &tipo);
                while (tipo != 1 && tipo != 2 && tipo != 3) {
                    scanf("%d", &tipo);
                }
                switch(tipo) {
                    case 1:
                        strcpy(agenda[nContactos - 1].tipo, "FAVORITO");
                        break;
                    case 2:
                        strcpy(agenda[nContactos - 1].tipo, "CONOCIDO");
                        break;
                    case 3:
                        strcpy(agenda[nContactos - 1].tipo, "TRABAJO");
                        break;
                    default:
                        printf("%d no es una opcion valida, elije una de las seis que hay.\n", opcion);
                }
                tipo = 0;
                break;
            default:
                printf("Has introducido un valor inválido.\n");
        }
        
    } while (opcion != 0);
            
    free(agenda);

    return 0;
}

void printContactos(int nContactos, tAgenda *agenda) {
    if (nContactos > 0) {
        for (int i = 0; i < nContactos; ++i) {
            printf("%s;%s;%s;%hi;%s\n", agenda[i].nombre, agenda[i].apellidos, agenda[i].telefono, agenda[i].edad, agenda[i].tipo);
        }
    }
    else printf("No hay contactos en la agenda aun.\n");
}
