//
// Created by ddeln on 18/04/2023.
//

#ifndef INC_4_18_FECHA_H
#define INC_4_18_FECHA_H

// Estructura que almacena dia, mes y año
typedef struct {
   int dia;
   int mes;
   int anyo;
} Fecha;

// Funcion que crea una fecha
Fecha *crearFecha(int dia, int mes, int anyo);
int obtenerDia(Fecha f);

#endif //INC_4_18_FECHA_H

