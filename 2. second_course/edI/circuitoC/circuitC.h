//
// Created by ddeln on 05/10/2023.
//

#ifndef CIRCUITOC_CIRCUITC_H
#define CIRCUITOC_CIRCUITC_H

#include "complexC.h"


// (* impedancias *)
tComplejo impedanciaL(double w, double l);
tComplejo impedanciaR(double r);
tComplejo impedanciaC(double w, double c);
tComplejo impedanciaTotal(tComplejo impedanciaL, tComplejo impedanciaR, tComplejo impedanciaC);


// (* frecuencia angular *)
double frecAngular(double v);


// (* ley de ohm *)
tComplejo intensidad(tComplejo v, tComplejo z);
tComplejo potencial(tComplejo i, tComplejo z);

#endif //CIRCUITOC_CIRCUITC_H
