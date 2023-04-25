#include <stdio.h>
#include "fecha.h"

int main() {
    Fecha *f = crearFecha(18, 4, 2023);

    printf("El dia es: %i\n", obtenerDia(*f));
    printf("El mes es: %i\n", f->mes);
    printf("El año es: %i\n", f->anyo);

    return 0;
}
