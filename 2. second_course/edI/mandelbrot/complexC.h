//
// Created by ddeln on 26/09/2023.
//

#ifndef INC_26_09_2023_COMPLEXC_H
#define INC_26_09_2023_COMPLEXC_H

#include <stdio.h>
#include <math.h>

typedef struct {
    double re;
    double im;
} tComplejo;

// (* constructoras generadoras *)
tComplejo complexCreate(double re, double im);

// (* observadoras selectoras *)
double complexObtenerReal(tComplejo c1);
double complexObtenerImaginaria(tComplejo c1);

// (* observadoras no selectoras *)
double complexModulo(tComplejo c1);

// (* constructoras no generadoras *)
tComplejo complexConjugado(tComplejo c1);
tComplejo complexSuma(tComplejo c1, tComplejo c2);
tComplejo complexResta(tComplejo c1, tComplejo c2);
tComplejo complexMultiplicacion(tComplejo c1, tComplejo c2);
tComplejo complexDivision(tComplejo c1, tComplejo c2);

#endif //INC_26_09_2023_COMPLEXC_H
