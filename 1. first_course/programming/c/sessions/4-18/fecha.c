//
// Created by ddeln on 18/04/2023.
//

#include "fecha.h"
#include <stdlib.h>

Fecha *crearFecha(int dia, int mes, int anyo) {
    Fecha *f = malloc(sizeof(Fecha));
    f->dia = dia;
    f->mes = mes;
    f->anyo = anyo;

    return f;
}

int obtenerDia(Fecha f) {
    return f.dia;
}