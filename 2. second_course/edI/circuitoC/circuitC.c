//
// Created by ddeln on 05/10/2023.
//

#include "circuitC.h"
const double pi = 3.14159265359;


// (* impedancias *)
tComplejo impedanciaL(double w, double l) {
    return complexMultiplicacion(complexCreate(w, 0), complexCreate(l, 0));
}
tComplejo impedanciaR(double r) {
    return complexCreate(r, 0);
}
tComplejo impedanciaC(double w, double c) {
    return complexDivision(complexCreate(1, 0),
                           complexMultiplicacion(complexCreate(w, 0), complexCreate(c, 0)));
}
tComplejo impedanciaTotal(tComplejo impedanciaL, tComplejo impedanciaR, tComplejo impedanciaC) {
    return complexSuma(complexSuma(impedanciaL, impedanciaR), impedanciaC);
}


// (* frecuencia angular *)
double frecAngular(double v) {
    return 2*pi*v;
}


// (* ley de ohm *)
tComplejo intensidad(tComplejo v, tComplejo z) {
    return complexDivision(v, z);
}
tComplejo potencial(tComplejo i, tComplejo z) {
    return complexMultiplicacion(i, z);
}